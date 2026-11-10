from decimal import Decimal
from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404, JsonResponse
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db import transaction
from django.db.models import Q, Count, Sum, F
from django.views.decorators.http import require_POST

from .models import Category, Product, Order, OrderItem, NewsletterSubscriber
from .forms import (
    UserRegistrationForm,
    UserLoginForm,
    UserProfileForm,
    CheckoutForm,
    NewsletterForm
)
from .cart import Cart


def home(request):
    """
    Homepage showcasing hero banner, top categories, featured products,
    new arrivals, best sellers, and newsletter signup.
    """
    categories = Category.objects.annotate(total_products=Count('products')).filter(total_products__gt=0)[:6]
    if not categories.exists():
        categories = Category.objects.all()[:6]

    active_products = Product.objects.filter(is_active=True).select_related('category')
    
    # Featured products: first 8 active products
    featured_products = active_products[:8]
    
    # New arrivals: sorted by creation date
    new_arrivals = active_products.order_by('-created_at')[:8]
    
    # Best-selling products based on actual order item records
    best_seller_ids = (
        OrderItem.objects.filter(product__is_active=True)
        .values('product')
        .annotate(total_sold=Sum('quantity'))
        .order_by('-total_sold')
        .values_list('product', flat=True)[:8]
    )
    if best_seller_ids:
        best_sellers = list(Product.objects.filter(id__in=best_seller_ids, is_active=True).select_related('category'))
        # Maintain order of best sellers
        id_order = {pid: i for i, pid in enumerate(best_seller_ids)}
        best_sellers.sort(key=lambda p: id_order.get(p.id, 999))
    else:
        # Fallback to top products if no orders placed yet
        best_sellers = list(active_products.order_by('price')[:8])

    total_catalog_products = active_products.count()

    context = {
        'categories': categories,
        'featured_products': featured_products,
        'new_arrivals': new_arrivals,
        'best_sellers': best_sellers,
        'total_catalog_products': total_catalog_products,
        'newsletter_form': NewsletterForm(),
    }
    return render(request, 'shop/home.html', context)


def product_list(request, category_slug=None):
    """
    Product listing catalogue with search, filtering by category, price,
    stock availability, sorting options, and pagination.
    """
    category = None
    categories = Category.objects.annotate(total_products=Count('products')).all()
    products_qs = Product.objects.filter(is_active=True).select_related('category')

    # Category filter via URL slug or GET parameter
    cat_param = category_slug or request.GET.get('category')
    if cat_param:
        category = get_object_or_404(Category, slug=cat_param)
        products_qs = products_qs.filter(category=category)

    # Search keyword
    query = request.GET.get('q', '').strip()
    if query:
        products_qs = products_qs.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query) |
            Q(category__name__icontains=query)
        )

    # Price range filters
    min_price = request.GET.get('min_price', '').strip()
    max_price = request.GET.get('max_price', '').strip()
    if min_price:
        try:
            products_qs = products_qs.filter(price__gte=Decimal(min_price))
        except (ValueError, ArithmeticError):
            pass

    if max_price:
        try:
            products_qs = products_qs.filter(price__lte=Decimal(max_price))
        except (ValueError, ArithmeticError):
            pass

    # In-stock filter
    in_stock_only = request.GET.get('in_stock', '').strip()
    if in_stock_only in ('1', 'true', 'yes'):
        products_qs = products_qs.filter(stock_quantity__gt=0)

    # Sorting
    sort_by = request.GET.get('sort', 'newest')
    if sort_by == 'price_low':
        products_qs = products_qs.order_by('price')
    elif sort_by == 'price_high':
        products_qs = products_qs.order_by('-price')
    elif sort_by == 'name':
        products_qs = products_qs.order_by('name')
    else:  # newest
        products_qs = products_qs.order_by('-created_at')

    # Pagination: 9 products per page
    paginator = Paginator(products_qs, 9)
    page_number = request.GET.get('page')
    try:
        page_obj = paginator.get_page(page_number)
    except (PageNotAnInteger, EmptyPage):
        page_obj = paginator.get_page(1)

    # Preserve GET parameters for pagination links
    query_params = request.GET.copy()
    if 'page' in query_params:
        query_params.pop('page')

    context = {
        'category': category,
        'categories': categories,
        'products': page_obj,
        'page_obj': page_obj,
        'total_count': products_qs.count(),
        'query': query,
        'min_price': min_price,
        'max_price': max_price,
        'in_stock_only': in_stock_only in ('1', 'true', 'yes'),
        'sort_by': sort_by,
        'query_string': query_params.urlencode(),
    }
    return render(request, 'shop/product_list.html', context)


def category_list(request):
    """
    Dedicated category browsing page showing all categories with product counts.
    """
    categories = Category.objects.annotate(total_products=Count('products')).all()
    context = {
        'categories': categories,
    }
    return render(request, 'shop/category_list.html', context)


def product_detail(request, slug):
    """
    Product details page with stock status, dynamic quantity selector,
    and related products from the same category.
    """
    # Active products for public, staff can preview inactive products
    if request.user.is_staff:
        product = get_object_or_404(Product, slug=slug)
    else:
        product = get_object_or_404(Product, slug=slug, is_active=True)

    # Related products from same category
    related_products = Product.objects.filter(
        category=product.category,
        is_active=True
    ).exclude(id=product.id)[:4]

    context = {
        'product': product,
        'related_products': related_products,
        'max_order_qty': min(product.stock_quantity, 10),
    }
    return render(request, 'shop/product_detail.html', context)


def cart_detail(request):
    """
    Shopping cart view displaying items, subtotals, shipping, and grand total.
    """
    cart = Cart(request)
    context = {
        'cart': cart,
        'subtotal': cart.get_subtotal_price(),
        'shipping': cart.get_shipping_price(),
        'total': cart.get_total_price(),
    }
    return render(request, 'shop/cart.html', context)


@require_POST
def cart_add(request, product_id):
    """
    Add product to shopping cart. Handles both standard form POST and AJAX requests.
    Validates stock availability on the server.
    """
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)

    try:
        quantity = int(request.POST.get('quantity', 1))
    except (ValueError, TypeError):
        quantity = 1

    override = request.POST.get('override') == 'True'

    is_ajax = request.headers.get('x-requested-with') == 'XMLHttpRequest'

    try:
        new_qty = cart.add(product=product, quantity=quantity, override_quantity=override)
        messages.success(request, f"Added {product.name} to your shopping cart.")
        if is_ajax:
            return JsonResponse({
                'success': True,
                'message': f"Added {product.name} to cart.",
                'cart_item_count': len(cart),
                'cart_subtotal': str(cart.get_subtotal_price()),
                'cart_total': str(cart.get_total_price()),
                'item_quantity': new_qty,
            })
    except ValueError as e:
        messages.error(request, str(e))
        if is_ajax:
            return JsonResponse({
                'success': False,
                'message': str(e),
                'cart_item_count': len(cart),
            }, status=400)

    # Redirect back to referring page or cart
    next_url = request.POST.get('next') or request.META.get('HTTP_REFERER') or 'shop:cart_detail'
    return redirect(next_url)


@require_POST
def cart_update(request, product_id):
    """
    Update item quantity in cart (+1, -1, or direct number).
    """
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    action = request.POST.get('action')

    current_item = cart.cart.get(str(product.id))
    current_qty = current_item['quantity'] if current_item else 0

    if action == 'increase':
        target_qty = current_qty + 1
    elif action == 'decrease':
        target_qty = current_qty - 1
    else:
        try:
            target_qty = int(request.POST.get('quantity', 1))
        except (ValueError, TypeError):
            target_qty = 1

    is_ajax = request.headers.get('x-requested-with') == 'XMLHttpRequest'

    try:
        if target_qty <= 0:
            cart.remove(product)
            messages.info(request, f"Removed {product.name} from your cart.")
            new_qty = 0
            item_subtotal = Decimal('0.00')
        else:
            new_qty = cart.update_quantity(product=product, quantity=target_qty)
            item_subtotal = product.price * new_qty
            messages.success(request, f"Updated quantity for {product.name}.")

        if is_ajax:
            return JsonResponse({
                'success': True,
                'cart_item_count': len(cart),
                'item_quantity': new_qty,
                'item_subtotal': str(item_subtotal),
                'subtotal': str(cart.get_subtotal_price()),
                'shipping': str(cart.get_shipping_price()),
                'total': str(cart.get_total_price()),
            })
    except ValueError as e:
        messages.error(request, str(e))
        if is_ajax:
            return JsonResponse({'success': False, 'message': str(e)}, status=400)

    return redirect('shop:cart_detail')


@require_POST
def cart_remove(request, product_id):
    """
    Remove an item completely from the cart.
    """
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    messages.info(request, f"Removed '{product.name}' from your cart.")
    return redirect('shop:cart_detail')


@require_POST
def cart_clear(request):
    """
    Clear all items from the cart.
    """
    cart = Cart(request)
    cart.clear()
    messages.info(request, "Your shopping cart has been cleared.")
    return redirect('shop:cart_detail')


@login_required
def checkout(request):
    """
    Checkout view.
    Validates delivery information, verifies current database stock,
    creates the Order and OrderItem snapshots atomically, reduces inventory,
    and clears the session cart.
    """
    cart = Cart(request)
    if len(cart) == 0:
        messages.warning(request, "Your cart is empty. Add products before proceeding to checkout.")
        return redirect('shop:product_list')

    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    # 1. Re-validate cart items against active database state and lock rows
                    cart_items = list(cart)
                    if not cart_items:
                        messages.error(request, "Your cart has no active items.")
                        return redirect('shop:cart_detail')

                    total_calculated = Decimal('0.00')

                    # Check stock for all items first
                    for item in cart_items:
                        # Lock product row for update to avoid race conditions
                        product = Product.objects.select_for_update().get(id=item['product'].id)
                        if not product.is_active:
                            raise ValueError(f"Product '{product.name}' is no longer active.")
                        if product.stock_quantity < item['quantity']:
                            raise ValueError(
                                f"Insufficient stock for '{product.name}'. "
                                f"Only {product.stock_quantity} left in stock, but you requested {item['quantity']}."
                            )
                        total_calculated += product.price * item['quantity']

                    # Add shipping calculation
                    shipping_charge = cart.get_shipping_price()
                    grand_total = total_calculated + shipping_charge

                    # 2. Create the Order
                    order = form.save(commit=False)
                    order.user = request.user
                    order.order_number = Order.generate_order_number()
                    order.total_amount = grand_total
                    order.order_status = Order.STATUS_PENDING
                    order.payment_status = Order.PAYMENT_STATUS_PENDING
                    order.save()

                    # 3. Create OrderItems & update product stock atomically
                    for item in cart_items:
                        product = Product.objects.select_for_update().get(id=item['product'].id)
                        OrderItem.objects.create(
                            order=order,
                            product=product,
                            product_name=product.name,
                            unit_price=product.price,
                            quantity=item['quantity'],
                            subtotal=product.price * item['quantity']
                        )
                        # Reduce stock
                        product.stock_quantity = F('stock_quantity') - item['quantity']
                        product.save(update_fields=['stock_quantity'])

                    # 4. Clear the cart
                    cart.clear()

                    messages.success(
                        request,
                        f"Your order #{order.order_number} has been placed successfully!"
                    )
                    return redirect('shop:order_confirmation', order_number=order.order_number)

            except ValueError as e:
                messages.error(request, str(e))
                return redirect('shop:cart_detail')
            except Exception as e:
                messages.error(request, f"An error occurred while placing your order: {str(e)}")
    else:
        # Pre-fill checkout form with user details
        initial_data = {
            'full_name': f"{request.user.first_name} {request.user.last_name}".strip() or request.user.username,
            'email': request.user.email,
        }
        form = CheckoutForm(initial=initial_data)

    context = {
        'form': form,
        'cart': cart,
        'subtotal': cart.get_subtotal_price(),
        'shipping': cart.get_shipping_price(),
        'total': cart.get_total_price(),
    }
    return render(request, 'shop/checkout.html', context)


@login_required
def order_confirmation(request, order_number):
    """
    Order success confirmation page.
    Restricted to the user who placed the order or staff.
    """
    if request.user.is_staff:
        order = get_object_or_404(Order, order_number=order_number)
    else:
        order = get_object_or_404(Order, order_number=order_number, user=request.user)

    context = {
        'order': order,
        'items': order.items.select_related('product').all(),
    }
    return render(request, 'shop/order_confirmation.html', context)


@login_required
def order_list(request):
    """
    List past orders for the authenticated user with status and details links.
    """
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    paginator = Paginator(orders, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'orders': page_obj,
        'page_obj': page_obj,
    }
    return render(request, 'shop/order_list.html', context)


@login_required
def order_detail(request, order_number):
    """
    Detailed order view. Strictly checked: customers cannot view other customers' orders.
    """
    if request.user.is_staff:
        order = get_object_or_404(Order, order_number=order_number)
    else:
        order = get_object_or_404(Order, order_number=order_number, user=request.user)

    context = {
        'order': order,
        'items': order.items.select_related('product').all(),
    }
    return render(request, 'shop/order_detail.html', context)


@login_required
@require_POST
def order_cancel(request, order_number):
    """
    Cancel an order if it is in Pending or Confirmed status.
    Automatically restores stock for each order item atomically.
    """
    if request.user.is_staff:
        order = get_object_or_404(Order, order_number=order_number)
    else:
        order = get_object_or_404(Order, order_number=order_number, user=request.user)

    if order.can_cancel:
        order.cancel_order()
        messages.success(request, f"Order #{order.order_number} has been cancelled and inventory restored.")
    else:
        messages.error(
            request,
            f"Order #{order.order_number} cannot be cancelled because its status is '{order.order_status}'."
        )

    return redirect('shop:order_detail', order_number=order.order_number)


def user_register(request):
    """
    User registration view.
    """
    if request.user.is_authenticated:
        return redirect('shop:home')

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Explicitly specify backend to avoid multiple backend ambiguity
            login(request, user, backend='shop.backends.EmailOrUsernameModelBackend')
            messages.success(
                request,
                f"Welcome to NovaMart, {user.first_name or user.username}! Your account has been registered."
            )
            next_url = request.GET.get('next') or 'shop:home'
            return redirect(next_url)
    else:
        form = UserRegistrationForm()

    context = {
        'form': form,
    }
    return render(request, 'shop/register.html', context)


def user_login(request):
    """
    User login view supporting username or email.
    """
    if request.user.is_authenticated:
        return redirect('shop:home')

    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user, backend='shop.backends.EmailOrUsernameModelBackend')
            messages.success(request, f"Welcome back, {user.first_name or user.username}!")
            next_url = request.GET.get('next') or request.POST.get('next') or 'shop:home'
            return redirect(next_url)
    else:
        form = UserLoginForm()

    context = {
        'form': form,
        'next': request.GET.get('next', ''),
    }
    return render(request, 'shop/login.html', context)


def user_logout(request):
    """
    User logout view. Accepts GET and POST.
    """
    if request.user.is_authenticated:
        logout(request)
        messages.info(request, "You have been logged out successfully. See you again soon!")
    return redirect('shop:home')


@login_required
def account_profile(request):
    """
    User account profile page with profile editing and recent orders overview.
    """
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Your profile details have been updated successfully.")
            return redirect('shop:account_profile')
    else:
        form = UserProfileForm(instance=request.user)

    recent_orders = Order.objects.filter(user=request.user).order_by('-created_at')[:5]
    total_orders_count = Order.objects.filter(user=request.user).count()

    context = {
        'form': form,
        'recent_orders': recent_orders,
        'total_orders_count': total_orders_count,
    }
    return render(request, 'shop/account.html', context)


@require_POST
def newsletter_subscribe(request):
    """
    Newsletter subscription endpoint with friendly feedback.
    """
    email = request.POST.get('email', '').strip().lower()
    is_ajax = request.headers.get('x-requested-with') == 'XMLHttpRequest'

    if not email or '@' not in email:
        msg = "Please enter a valid email address."
        if is_ajax:
            return JsonResponse({'success': False, 'message': msg}, status=400)
        messages.error(request, msg)
        return redirect(request.META.get('HTTP_REFERER', 'shop:home'))

    sub, created = NewsletterSubscriber.objects.get_or_create(email=email)
    if created:
        msg = "Thank you for subscribing to NovaMart's newsletter!"
        if is_ajax:
            return JsonResponse({'success': True, 'message': msg})
        messages.success(request, msg)
    else:
        msg = "You are already subscribed with this email address."
        if is_ajax:
            return JsonResponse({'success': True, 'message': msg})
        messages.info(request, msg)

    return redirect(request.META.get('HTTP_REFERER', 'shop:home'))


def custom_404_view(request, exception=None):
    """Custom 404 page"""
    return render(request, 'shop/404.html', status=404)


def custom_500_view(request):
    """Custom 500 page"""
    return render(request, 'shop/500.html', status=500)
