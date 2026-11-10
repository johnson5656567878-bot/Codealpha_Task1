from django.conf import settings
from .cart import Cart
from .models import Category


def shop_context(request):
    """
    Context processor making cart information, categories, and currency
    available globally across all templates.
    """
    cart = Cart(request)
    return {
        'cart': cart,
        'cart_item_count': len(cart),
        'cart_subtotal': cart.get_subtotal_price(),
        'cart_total': cart.get_total_price(),
        'nav_categories': Category.objects.all()[:10],
        'CURRENCY_SYMBOL': getattr(settings, 'CURRENCY_SYMBOL', '₹'),
    }
