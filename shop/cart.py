from decimal import Decimal
from django.conf import settings
from .models import Product


class Cart:
    """
    Session-based shopping cart.
    Stores product IDs and quantities in the user session.
    All prices and stock validations are calculated dynamically from database models.
    """

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity=1, override_quantity=False):
        """
        Add a product to the cart or update its quantity.
        Validates stock availability on the server.
        Raises ValueError if requested quantity exceeds available stock.
        """
        if not product.is_active:
            raise ValueError(f"Product '{product.name}' is currently unavailable.")

        if product.stock_quantity <= 0:
            raise ValueError(f"Product '{product.name}' is out of stock.")

        product_id = str(product.id)
        current_qty = self.cart.get(product_id, {}).get('quantity', 0)

        if override_quantity:
            new_qty = quantity
        else:
            new_qty = current_qty + quantity

        if new_qty <= 0:
            self.remove(product)
            return 0

        # Enforce server-side stock limit
        if new_qty > product.stock_quantity:
            raise ValueError(
                f"Cannot add {new_qty} units. Only {product.stock_quantity} available in stock for '{product.name}'."
            )

        self.cart[product_id] = {
            'quantity': new_qty,
            'price': str(product.price),
        }
        self.save()
        return new_qty

    def update_quantity(self, product, quantity):
        """Update product quantity directly."""
        return self.add(product, quantity=quantity, override_quantity=True)

    def remove(self, product):
        """Remove a product completely from the cart."""
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def clear(self):
        """Empty the cart session."""
        self.cart = {}
        if settings.CART_SESSION_ID in self.session:
            del self.session[settings.CART_SESSION_ID]
        self.session.modified = True

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def __iter__(self):
        """
        Iterate over the items in the cart and query current product records from the database.
        Calculates subtotals using Decimal type.
        """
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids, is_active=True).select_related('category')
        product_map = {str(p.id): p for p in products}

        # Clean up any products that no longer exist or are inactive
        missing_ids = [pid for pid in product_ids if pid not in product_map]
        for mid in missing_ids:
            del self.cart[mid]
        if missing_ids:
            self.save()

        for product_id, item_data in self.cart.items():
            product = product_map.get(product_id)
            if not product:
                continue

            quantity = item_data['quantity']
            # Re-cap quantity if stock decreased since item was added
            if quantity > product.stock_quantity:
                quantity = max(0, product.stock_quantity)
                item_data['quantity'] = quantity
                self.save()

            if quantity == 0:
                continue

            unit_price = product.price
            subtotal = unit_price * quantity
            yield {
                'product': product,
                'quantity': quantity,
                'unit_price': unit_price,
                'subtotal': subtotal,
                'max_stock': product.stock_quantity,
            }

    def __len__(self):
        """Return total number of items in the cart."""
        return sum(item['quantity'] for item in self.cart.values())

    def get_subtotal_price(self):
        """Calculate total amount for all items in the cart."""
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids, is_active=True)
        product_map = {str(p.id): p for p in products}
        total = Decimal('0.00')

        for product_id, item_data in self.cart.items():
            product = product_map.get(product_id)
            if product and product.stock_quantity > 0:
                qty = min(item_data['quantity'], product.stock_quantity)
                total += product.price * qty

        return total

    def get_shipping_price(self):
        """Free shipping for orders >= ₹999, else flat ₹99."""
        subtotal = self.get_subtotal_price()
        if subtotal == Decimal('0.00') or subtotal >= Decimal('999.00'):
            return Decimal('0.00')
        return Decimal('99.00')

    def get_total_price(self):
        """Calculate final order total including shipping."""
        return self.get_subtotal_price() + self.get_shipping_price()
