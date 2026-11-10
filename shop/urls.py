from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    # Homepage
    path('', views.home, name='home'),

    # Product Catalog & Categories
    path('products/', views.product_list, name='product_list'),
    path('products/category/<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('categories/', views.category_list, name='category_list'),
    path('products/<slug:slug>/', views.product_detail, name='product_detail'),

    # Shopping Cart
    path('cart/', views.cart_detail, name='cart_detail'),
    path('cart/add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('cart/update/<int:product_id>/', views.cart_update, name='cart_update'),
    path('cart/remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
    path('cart/clear/', views.cart_clear, name='cart_clear'),

    # Checkout & Orders
    path('checkout/', views.checkout, name='checkout'),
    path('orders/', views.order_list, name='order_list'),
    path('orders/<str:order_number>/details/', views.order_detail, name='order_detail'),
    path('orders/<str:order_number>/cancel/', views.order_cancel, name='order_cancel'),
    path('orders/<str:order_number>/', views.order_confirmation, name='order_confirmation'),

    # User Authentication & Profile
    path('accounts/register/', views.user_register, name='register'),
    path('accounts/login/', views.user_login, name='login'),
    path('accounts/logout/', views.user_logout, name='logout'),
    path('account/', views.account_profile, name='account_profile'),

    # Newsletter
    path('newsletter/subscribe/', views.newsletter_subscribe, name='newsletter_subscribe'),
]
