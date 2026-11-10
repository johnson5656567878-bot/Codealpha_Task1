/**
 * NovaMart Interactive JavaScript
 * Handles AJAX cart operations, live counter updates, quantity steppers,
 * toast notifications, and interactive filters.
 */

document.addEventListener('DOMContentLoaded', () => {
  initCartSteppers();
  initAddToCartForms();
  initAutoDismissAlerts();
  initNewsletterForm();
});

/**
 * Retrieve CSRF token from document cookies or hidden inputs
 */
function getCsrfToken() {
  const tokenInput = document.querySelector('[name=csrfmiddlewaretoken]');
  if (tokenInput) return tokenInput.value;

  const cookie = document.cookie
    .split('; ')
    .find(row => row.startsWith('csrftoken='));
  return cookie ? decodeURIComponent(cookie.split('=')[1]) : '';
}

/**
 * Format number as Indian Rupee string (e.g. ₹1,299.00)
 */
function formatCurrency(amount) {
  const num = parseFloat(amount);
  if (isNaN(num)) return '₹0.00';
  return '₹' + num.toLocaleString('en-IN', { minimumFractionDigits: 2, maximumFractionDigits: 2 });
}

/**
 * Update the navbar cart counter badge
 */
function updateNavbarCartCount(count) {
  const badges = document.querySelectorAll('.cart-counter');
  badges.forEach(badge => {
    badge.textContent = count;
    if (count > 0) {
      badge.style.display = 'flex';
      badge.classList.remove('pulse-animation');
      void badge.offsetWidth; // trigger reflow
      badge.classList.add('pulse-animation');
    } else {
      badge.style.display = 'none';
    }
  });
}

/**
 * Show a sleek floating toast notification
 */
function showToast(message, type = 'success') {
  let container = document.getElementById('toastContainer');
  if (!container) {
    container = document.createElement('div');
    container.id = 'toastContainer';
    container.className = 'toast-container-custom';
    document.body.appendChild(container);
  }

  const toast = document.createElement('div');
  toast.className = `toast-custom alert-${type}`;
  
  let iconClass = 'bi-check-circle-fill text-success';
  if (type === 'danger' || type === 'error') iconClass = 'bi-exclamation-triangle-fill text-danger';
  if (type === 'info') iconClass = 'bi-info-circle-fill text-info';
  if (type === 'warning') iconClass = 'bi-exclamation-circle-fill text-warning';

  toast.innerHTML = `
    <i class="bi ${iconClass} fs-5"></i>
    <div class="flex-grow-1">
      <div class="fw-semibold text-dark fs-6">${message}</div>
    </div>
    <button type="button" class="btn-close ms-2" aria-label="Close"></button>
  `;

  const closeBtn = toast.querySelector('.btn-close');
  closeBtn.addEventListener('click', () => {
    toast.remove();
  });

  container.appendChild(toast);

  setTimeout(() => {
    toast.style.opacity = '0';
    toast.style.transform = 'translateX(50px)';
    toast.style.transition = 'all 0.3s ease';
    setTimeout(() => toast.remove(), 300);
  }, 4500);
}

/**
 * Quantity stepper buttons and dynamic update on Cart page
 */
function initCartSteppers() {
  document.querySelectorAll('.qty-stepper').forEach(stepper => {
    const input = stepper.querySelector('input.qty-input');
    const btnMinus = stepper.querySelector('.btn-qty-minus');
    const btnPlus = stepper.querySelector('.btn-qty-plus');
    if (!input) return;

    const maxStock = parseInt(input.getAttribute('max')) || 999;
    const minVal = parseInt(input.getAttribute('min')) || 1;
    const productId = stepper.dataset.productId;
    const isCartTable = stepper.dataset.isCart === 'true';

    function updateButtons(val) {
      if (btnMinus) btnMinus.disabled = val <= minVal;
      if (btnPlus) btnPlus.disabled = val >= maxStock;
    }

    updateButtons(parseInt(input.value) || minVal);

    if (btnMinus) {
      btnMinus.addEventListener('click', (e) => {
        e.preventDefault();
        let cur = parseInt(input.value) || minVal;
        if (cur > minVal) {
          cur -= 1;
          input.value = cur;
          updateButtons(cur);
          if (isCartTable && productId) {
            sendCartUpdate(productId, 'decrease', cur);
          }
        }
      });
    }

    if (btnPlus) {
      btnPlus.addEventListener('click', (e) => {
        e.preventDefault();
        let cur = parseInt(input.value) || minVal;
        if (cur < maxStock) {
          cur += 1;
          input.value = cur;
          updateButtons(cur);
          if (isCartTable && productId) {
            sendCartUpdate(productId, 'increase', cur);
          }
        } else {
          showToast(`Only ${maxStock} items available in stock.`, 'warning');
        }
      });
    }

    input.addEventListener('change', () => {
      let val = parseInt(input.value);
      if (isNaN(val) || val < minVal) val = minVal;
      if (val > maxStock) {
        val = maxStock;
        showToast(`Stock limit reached! Max available is ${maxStock}.`, 'warning');
      }
      input.value = val;
      updateButtons(val);
      if (isCartTable && productId) {
        sendCartUpdate(productId, 'set', val);
      }
    });
  });
}

/**
 * Send async update to cart endpoint and recalculate totals
 */
function sendCartUpdate(productId, action, quantity) {
  const formData = new FormData();
  formData.append('action', action);
  formData.append('quantity', quantity);

  fetch(`/cart/update/${productId}/`, {
    method: 'POST',
    headers: {
      'X-CSRFToken': getCsrfToken(),
      'X-Requested-With': 'XMLHttpRequest'
    },
    body: formData
  })
  .then(res => res.json())
  .then(data => {
    if (data.success) {
      updateNavbarCartCount(data.cart_item_count);

      // If quantity became 0, remove the row
      const row = document.getElementById(`cart-row-${productId}`);
      if (data.item_quantity === 0 && row) {
        row.remove();
        if (data.cart_item_count === 0) {
          window.location.reload();
          return;
        }
      }

      // Update line subtotal
      const lineSubtotalEl = document.getElementById(`line-subtotal-${productId}`);
      if (lineSubtotalEl && data.item_subtotal) {
        lineSubtotalEl.textContent = formatCurrency(data.item_subtotal);
      }

      // Update summary card
      const summarySubtotal = document.getElementById('summary-subtotal');
      const summaryShipping = document.getElementById('summary-shipping');
      const summaryTotal = document.getElementById('summary-total');

      if (summarySubtotal) summarySubtotal.textContent = formatCurrency(data.subtotal);
      if (summaryShipping) {
        const shipVal = parseFloat(data.shipping);
        summaryShipping.textContent = shipVal === 0 ? 'FREE' : formatCurrency(shipVal);
      }
      if (summaryTotal) summaryTotal.textContent = formatCurrency(data.total);

      showToast('Cart updated successfully.', 'success');
    } else {
      showToast(data.message || 'Failed to update cart.', 'danger');
    }
  })
  .catch(err => {
    console.error('Cart update error:', err);
  });
}

/**
 * Handle async Add-To-Cart submissions
 */
function initAddToCartForms() {
  document.querySelectorAll('form.ajax-add-to-cart').forEach(form => {
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      const submitBtn = form.querySelector('button[type=submit]');
      const originalHtml = submitBtn ? submitBtn.innerHTML : '';
      if (submitBtn) {
        submitBtn.disabled = true;
        submitBtn.innerHTML = '<span class="spinner-border spinner-border-sm me-1" role="status"></span> Adding...';
      }

      const formData = new FormData(form);

      fetch(form.action, {
        method: 'POST',
        headers: {
          'X-CSRFToken': getCsrfToken(),
          'X-Requested-With': 'XMLHttpRequest'
        },
        body: formData
      })
      .then(res => res.json())
      .then(data => {
        if (data.success) {
          updateNavbarCartCount(data.cart_item_count);
          showToast(data.message || 'Added to cart!', 'success');
        } else {
          showToast(data.message || 'Could not add product.', 'danger');
        }
      })
      .catch(err => {
        console.error('Add to cart error:', err);
        // Fall back to standard submission if network error
        form.submit();
      })
      .finally(() => {
        if (submitBtn) {
          submitBtn.disabled = false;
          submitBtn.innerHTML = originalHtml;
        }
      });
    });
  });
}

/**
 * Auto-dismiss native Django messages after 5 seconds
 */
function initAutoDismissAlerts() {
  const alerts = document.querySelectorAll('.alert-dismissible');
  alerts.forEach(alert => {
    setTimeout(() => {
      alert.classList.add('fade');
      setTimeout(() => alert.remove(), 400);
    }, 5000);
  });
}

/**
 * Newsletter submission with AJAX
 */
function initNewsletterForm() {
  const form = document.getElementById('newsletterForm');
  if (!form) return;

  form.addEventListener('submit', (e) => {
    e.preventDefault();
    const input = form.querySelector('input[type=email]');
    const submitBtn = form.querySelector('button[type=submit]');
    if (!input || !input.value) return;

    if (submitBtn) submitBtn.disabled = true;

    const formData = new FormData(form);

    fetch(form.action, {
      method: 'POST',
      headers: {
        'X-CSRFToken': getCsrfToken(),
        'X-Requested-With': 'XMLHttpRequest'
      },
      body: formData
    })
    .then(res => res.json())
    .then(data => {
      showToast(data.message, data.success ? 'success' : 'danger');
      if (data.success) {
        input.value = '';
      }
    })
    .catch(err => {
      console.error('Newsletter error:', err);
      form.submit();
    })
    .finally(() => {
      if (submitBtn) submitBtn.disabled = false;
    });
  });
}
