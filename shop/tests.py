from decimal import Decimal
from django.conf import settings
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from shop.models import Category, Product, Order, OrderItem
from shop.cart import Cart

User = get_user_model()


class AuthenticationTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.register_url = reverse('shop:register')
        self.login_url = reverse('shop:login')
        self.logout_url = reverse('shop:logout')

    def test_user_registration_success(self):
        response = self.client.post(self.register_url, {
            'first_name': 'Aarav',
            'last_name': 'Patel',
            'username': 'aaravp',
            'email': 'aarav@example.com',
            'password': 'SecurePassword123!',
            'confirm_password': 'SecurePassword123!',
        })
        self.assertEqual(response.status_code, 302)
        user = User.objects.get(username='aaravp')
        self.assertEqual(user.email, 'aarav@example.com')
        # Check password is never stored plain text
        self.assertNotEqual(user.password, 'SecurePassword123!')
        self.assertTrue(user.check_password('SecurePassword123!'))

    def test_registration_password_mismatch(self):
        response = self.client.post(self.register_url, {
            'first_name': 'Test',
            'last_name': 'User',
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'Password123!',
            'confirm_password': 'DifferentPassword456!',
        })
        self.assertEqual(response.status_code, 200)
        self.assertFalse(User.objects.filter(username='testuser').exists())

    def test_registration_duplicate_username_prevented(self):
        User.objects.create_user(username='existinguser', email='exist@example.com', password='Password123!')
        response = self.client.post(self.register_url, {
            'first_name': 'Another',
            'last_name': 'User',
            'username': 'existinguser',
            'email': 'new@example.com',
            'password': 'Password123!',
            'confirm_password': 'Password123!',
        })
        self.assertEqual(response.status_code, 200)
        self.assertFormError(response.context['form'], 'username', "A user with this username already exists.")

    def test_login_with_username(self):
        User.objects.create_user(username='john_doe', email='john@example.com', password='MySecretPassword1')
        response = self.client.post(self.login_url, {
            'username': 'john_doe',
            'password': 'MySecretPassword1'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue('_auth_user_id' in self.client.session)

    def test_login_with_email_address(self):
        User.objects.create_user(username='priya_k', email='priya@example.com', password='MySecretPassword1')
        response = self.client.post(self.login_url, {
            'username': 'priya@example.com',
            'password': 'MySecretPassword1'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue('_auth_user_id' in self.client.session)

    def test_logout(self):
        user = User.objects.create_user(username='logout_user', password='Password123!')
        self.client.force_login(user)
        response = self.client.get(self.logout_url)
        self.assertEqual(response.status_code, 302)
        self.assertFalse('_auth_user_id' in self.client.session)


class CatalogAndProductTests(TestCase):
    def setUp(self):
        self.category_tech = Category.objects.create(name='Tech', slug='tech', description='Gadgets')
        self.category_fashion = Category.objects.create(name='Fashion', slug='fashion', description='Clothes')

        self.prod1 = Product.objects.create(
            category=self.category_tech,
            name='Noise Cancelling Headphones',
            slug='noise-cancelling-headphones',
            description='Wireless studio audio',
            price=Decimal('2999.00'),
            stock_quantity=10,
            is_active=True
        )
        self.prod2 = Product.objects.create(
            category=self.category_fashion,
            name='Cotton Casual T-Shirt',
            slug='cotton-casual-t-shirt',
            description='100% organic cotton tee',
            price=Decimal('699.00'),
            stock_quantity=0, # Out of stock
            is_active=True
        )
        self.prod_inactive = Product.objects.create(
            category=self.category_tech,
            name='Discontinued Phone',
            slug='discontinued-phone',
            description='Old model',
            price=Decimal('9999.00'),
            stock_quantity=5,
            is_active=False
        )

    def test_product_list_view(self):
        response = self.client.get(reverse('shop:product_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Noise Cancelling Headphones')
        self.assertContains(response, 'Cotton Casual T-Shirt')
        self.assertNotContains(response, 'Discontinued Phone')

    def test_product_list_filter_category(self):
        response = self.client.get(reverse('shop:product_list_by_category', args=['tech']))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Noise Cancelling Headphones')
        self.assertNotContains(response, 'Cotton Casual T-Shirt')

    def test_product_search(self):
        response = self.client.get(reverse('shop:product_list') + '?q=cotton')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Cotton Casual T-Shirt')
        self.assertNotContains(response, 'Noise Cancelling Headphones')

    def test_product_detail_view(self):
        response = self.client.get(reverse('shop:product_detail', args=[self.prod1.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Noise Cancelling Headphones')
        self.assertContains(response, '2999.00')

    def test_inactive_product_returns_404_for_customer(self):
        response = self.client.get(reverse('shop:product_detail', args=[self.prod_inactive.slug]))
        self.assertEqual(response.status_code, 404)

    def test_nonexistent_product_returns_404(self):
        response = self.client.get(reverse('shop:product_detail', args=['non-existent-product-slug']))
        self.assertEqual(response.status_code, 404)


class ShoppingCartTests(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Audio', slug='audio')
        self.product = Product.objects.create(
            category=self.category,
            name='Bluetooth Speaker',
            slug='bluetooth-speaker',
            description='Portable speaker',
            price=Decimal('1500.00'),
            stock_quantity=5,
            is_active=True
        )
        self.out_of_stock_product = Product.objects.create(
            category=self.category,
            name='Sold Out Earphones',
            slug='sold-out-earphones',
            description='Sold out',
            price=Decimal('500.00'),
            stock_quantity=0,
            is_active=True
        )

    def test_add_to_cart_operation(self):
        response = self.client.post(reverse('shop:cart_add', args=[self.product.id]), {
            'quantity': 2
        })
        self.assertEqual(response.status_code, 302)
        cart = Cart(response.wsgi_request)
        self.assertEqual(len(cart), 2)
        self.assertEqual(cart.get_subtotal_price(), Decimal('3000.00'))

    def test_reject_adding_exceeding_stock(self):
        # Only 5 in stock, attempting to add 10
        response = self.client.post(reverse('shop:cart_add', args=[self.product.id]), {
            'quantity': 10
        })
        cart = Cart(response.wsgi_request)
        self.assertEqual(len(cart), 0)

    def test_reject_out_of_stock_product(self):
        response = self.client.post(reverse('shop:cart_add', args=[self.out_of_stock_product.id]), {
            'quantity': 1
        })
        cart = Cart(response.wsgi_request)
        self.assertEqual(len(cart), 0)

    def test_update_and_remove_cart_item(self):
        # Add 1 item
        self.client.post(reverse('shop:cart_add', args=[self.product.id]), {'quantity': 1})
        # Update to 3 items
        self.client.post(reverse('shop:cart_update', args=[self.product.id]), {'quantity': 3})
        # Check subtotal
        response = self.client.get(reverse('shop:cart_detail'))
        self.assertContains(response, '4500.00')

        # Remove item
        self.client.post(reverse('shop:cart_remove', args=[self.product.id]))
        response = self.client.get(reverse('shop:cart_detail'))
        self.assertContains(response, 'Your Shopping Cart is Empty')


class CheckoutAndOrderTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='buyer',
            email='buyer@example.com',
            password='Password123!',
            first_name='Buyer',
            last_name='User'
        )
        self.other_user = User.objects.create_user(
            username='stranger',
            email='stranger@example.com',
            password='Password123!'
        )
        self.category = Category.objects.create(name='Gear', slug='gear')
        self.product = Product.objects.create(
            category=self.category,
            name='Camping Tent',
            slug='camping-tent',
            description='Waterproof dome tent',
            price=Decimal('2500.00'),
            stock_quantity=4,
            is_active=True
        )

    def test_checkout_requires_login(self):
        response = self.client.get(reverse('shop:checkout'))
        self.assertEqual(response.status_code, 302)
        self.assertIn(reverse('shop:login'), response.url)

    def test_checkout_redirects_if_cart_empty(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('shop:checkout'))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('shop:product_list'))

    def test_successful_order_placement_and_inventory_reduction(self):
        self.client.force_login(self.user)
        # Add 2 tents to cart
        self.client.post(reverse('shop:cart_add', args=[self.product.id]), {'quantity': 2})

        checkout_data = {
            'full_name': 'Buyer User',
            'email': 'buyer@example.com',
            'phone': '+91 9876543210',
            'delivery_address': 'Flat 101, Lake View Apts',
            'city': 'Bengaluru',
            'state': 'Karnataka',
            'postal_code': '560001',
            'payment_method': 'COD',
        }
        response = self.client.post(reverse('shop:checkout'), checkout_data)
        self.assertEqual(response.status_code, 302)

        # Verify Order record created
        order = Order.objects.filter(user=self.user).first()
        self.assertIsNotNone(order)
        self.assertEqual(order.payment_method, 'COD')
        self.assertEqual(order.order_status, Order.STATUS_PENDING)
        # Free delivery over ₹999, so total = 2500 * 2 = 5000.00
        self.assertEqual(order.total_amount, Decimal('5000.00'))

        # Verify OrderItem snapshots
        item = order.items.first()
        self.assertEqual(item.product_name, 'Camping Tent')
        self.assertEqual(item.unit_price, Decimal('2500.00'))
        self.assertEqual(item.quantity, 2)
        self.assertEqual(item.subtotal, Decimal('5000.00'))

        # Verify Inventory reduced from 4 to 2
        self.product.refresh_from_db()
        self.assertEqual(self.product.stock_quantity, 2)

        # Verify cart cleared
        cart_in_session = self.client.session.get(settings.CART_SESSION_ID, {})
        self.assertEqual(len(cart_in_session), 0)

    def test_order_privacy_protection(self):
        # Create an order under self.user
        order = Order.objects.create(
            order_number='ORD-TEST-PRIVACY',
            user=self.user,
            full_name='Buyer User',
            email='buyer@example.com',
            phone='9876543210',
            delivery_address='Address',
            city='City',
            state='State',
            postal_code='123456',
            total_amount=Decimal('1000.00'),
            order_status=Order.STATUS_PENDING
        )

        # Stranger attempts to view buyer's order
        self.client.force_login(self.other_user)
        response = self.client.get(reverse('shop:order_detail', args=[order.order_number]))
        self.assertEqual(response.status_code, 404)

        # Owner can view their own order
        self.client.force_login(self.user)
        response = self.client.get(reverse('shop:order_detail', args=[order.order_number]))
        self.assertEqual(response.status_code, 200)

    def test_order_cancellation_and_inventory_restoration(self):
        self.client.force_login(self.user)
        # Order with 2 units
        order = Order.objects.create(
            order_number='ORD-TEST-CANCEL',
            user=self.user,
            full_name='Buyer User',
            email='buyer@example.com',
            phone='9876543210',
            delivery_address='Address',
            city='City',
            state='State',
            postal_code='123456',
            total_amount=Decimal('5000.00'),
            order_status=Order.STATUS_PENDING
        )
        OrderItem.objects.create(
            order=order,
            product=self.product,
            product_name=self.product.name,
            unit_price=self.product.price,
            quantity=2,
            subtotal=Decimal('5000.00')
        )
        self.product.stock_quantity = 2
        self.product.save()

        # Cancel the order
        response = self.client.post(reverse('shop:order_cancel', args=[order.order_number]))
        self.assertEqual(response.status_code, 302)

        order.refresh_from_db()
        self.assertEqual(order.order_status, Order.STATUS_CANCELLED)

        # Stock restored: 2 + 2 = 4
        self.product.refresh_from_db()
        self.assertEqual(self.product.stock_quantity, 4)

    def test_admin_panel_access_restriction(self):
        # Regular customer cannot access admin
        self.client.force_login(self.user)
        response = self.client.get('/admin/')
        # Should redirect to login or deny
        self.assertIn(response.status_code, [302, 403])

        # Staff user can access admin
        staff_user = User.objects.create_superuser(
            username='staffadmin',
            email='admin@example.com',
            password='AdminPassword123!'
        )
        self.client.force_login(staff_user)
        response = self.client.get('/admin/')
        self.assertEqual(response.status_code, 200)
