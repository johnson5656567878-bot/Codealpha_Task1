from decimal import Decimal
import uuid
from django.db import models, transaction
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.urls import reverse

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=160, unique=True, db_index=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='categories/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='products'
    )
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=260, unique=True, db_index=True)
    description = models.TextField()
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0.01'))]
    )
    image = models.ImageField(upload_to='products/%Y/%m/', blank=True, null=True)
    stock_quantity = models.PositiveIntegerField(
        default=0,
        validators=[MinValueValidator(0)]
    )
    is_active = models.BooleanField(default=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['name']),
            models.Index(fields=['price']),
            models.Index(fields=['-created_at']),
        ]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.slug])

    @property
    def is_in_stock(self):
        return self.stock_quantity > 0 and self.is_active

    @property
    def get_image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        return '/static/shop/images/placeholder.svg'


class Order(models.Model):
    STATUS_PENDING = 'Pending'
    STATUS_CONFIRMED = 'Confirmed'
    STATUS_PROCESSING = 'Processing'
    STATUS_SHIPPED = 'Shipped'
    STATUS_DELIVERED = 'Delivered'
    STATUS_CANCELLED = 'Cancelled'

    ORDER_STATUS_CHOICES = [
        (STATUS_PENDING, 'Pending'),
        (STATUS_CONFIRMED, 'Confirmed'),
        (STATUS_PROCESSING, 'Processing'),
        (STATUS_SHIPPED, 'Shipped'),
        (STATUS_DELIVERED, 'Delivered'),
        (STATUS_CANCELLED, 'Cancelled'),
    ]

    PAYMENT_METHOD_COD = 'COD'
    PAYMENT_METHOD_CHOICES = [
        (PAYMENT_METHOD_COD, 'Cash on Delivery (COD)'),
    ]

    PAYMENT_STATUS_PENDING = 'Pending'
    PAYMENT_STATUS_PAID = 'Paid'
    PAYMENT_STATUS_FAILED = 'Failed'

    PAYMENT_STATUS_CHOICES = [
        (PAYMENT_STATUS_PENDING, 'Pending'),
        (PAYMENT_STATUS_PAID, 'Paid'),
        (PAYMENT_STATUS_FAILED, 'Failed'),
    ]

    order_number = models.CharField(max_length=64, unique=True, editable=False, db_index=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=25)
    delivery_address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    total_amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0.00'))]
    )
    payment_method = models.CharField(
        max_length=30,
        choices=PAYMENT_METHOD_CHOICES,
        default=PAYMENT_METHOD_COD
    )
    payment_status = models.CharField(
        max_length=30,
        choices=PAYMENT_STATUS_CHOICES,
        default=PAYMENT_STATUS_PENDING
    )
    order_status = models.CharField(
        max_length=30,
        choices=ORDER_STATUS_CHOICES,
        default=STATUS_PENDING,
        db_index=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Order #{self.order_number}"

    @classmethod
    def generate_order_number(cls):
        """Generates a unique, collision-resistant order number like ORD-20261022-A1B2C3D4"""
        from django.utils import timezone
        now_str = timezone.now().strftime('%Y%m%d')
        unique_token = uuid.uuid4().hex[:8].upper()
        return f"ORD-{now_str}-{unique_token}"

    @property
    def can_cancel(self):
        """Customers can only cancel orders in Pending or Confirmed status."""
        return self.order_status in [self.STATUS_PENDING, self.STATUS_CONFIRMED]

    @transaction.atomic
    def cancel_order(self):
        """
        Cancels the order and automatically restores stock for each item.
        Returns True if cancelled successfully, False otherwise.
        """
        if not self.can_cancel:
            return False

        for item in self.items.select_related('product').all():
            if item.product:
                # Atomically restore inventory
                item.product.stock_quantity = models.F('stock_quantity') + item.quantity
                item.product.save(update_fields=['stock_quantity'])

        self.order_status = self.STATUS_CANCELLED
        self.save(update_fields=['order_status', 'updated_at'])
        return True


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True, related_name='order_items')
    product_name = models.CharField(max_length=255)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    subtotal = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f"{self.quantity}x {self.product_name} (Order {self.order.order_number})"


class NewsletterSubscriber(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-subscribed_at']

    def __str__(self):
        return self.email
