from django.contrib import admin
from django.utils.html import format_html
from .models import Category, Product, Order, OrderItem, NewsletterSubscriber


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'product_count', 'created_at']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name', 'description']
    ordering = ['name']

    def product_count(self, obj):
        return obj.products.count()
    product_count.short_description = 'Products'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['image_preview', 'name', 'category', 'price', 'stock_quantity', 'stock_status', 'is_active', 'updated_at']
    list_filter = ['is_active', 'category', 'created_at']
    list_editable = ['price', 'stock_quantity', 'is_active']
    search_fields = ['name', 'description', 'category__name']
    prepopulated_fields = {'slug': ('name',)}
    ordering = ['-created_at']
    readonly_fields = ['image_preview_large', 'created_at', 'updated_at']
    fieldsets = (
        ('General Information', {
            'fields': ('name', 'slug', 'category', 'description')
        }),
        ('Pricing & Inventory', {
            'fields': ('price', 'stock_quantity', 'is_active')
        }),
        ('Media', {
            'fields': ('image', 'image_preview_large')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 45px; height: 45px; object-fit: cover; border-radius: 4px;" />', obj.image.url)
        return format_html('<span style="color: #999;">No image</span>')
    image_preview.short_description = 'Thumb'

    def image_preview_large(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-width: 250px; max-height: 250px; border-radius: 8px;" />', obj.image.url)
        return 'No image uploaded.'
    image_preview_large.short_description = 'Image Preview'

    def stock_status(self, obj):
        if obj.stock_quantity == 0:
            return format_html('<span style="color: #dc3545; font-weight: bold;">Out of Stock</span>')
        elif obj.stock_quantity <= 5:
            return format_html('<span style="color: #ffc107; font-weight: bold;">Low Stock ({})</span>', obj.stock_quantity)
        return format_html('<span style="color: #198754;">In Stock ({})</span>', obj.stock_quantity)
    stock_status.short_description = 'Availability'


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ['product', 'product_name', 'unit_price', 'quantity', 'subtotal']
    can_delete = False


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'order_number',
        'full_name',
        'user',
        'total_amount',
        'payment_method',
        'payment_status',
        'order_status',
        'created_at'
    ]
    list_filter = ['order_status', 'payment_status', 'payment_method', 'created_at']
    search_fields = ['order_number', 'full_name', 'email', 'phone', 'user__username']
    readonly_fields = ['order_number', 'created_at', 'updated_at', 'total_amount']
    inlines = [OrderItemInline]
    ordering = ['-created_at']
    actions = ['mark_as_confirmed', 'mark_as_processing', 'mark_as_shipped', 'mark_as_delivered', 'mark_as_paid']

    @admin.action(description="Mark selected orders as Confirmed")
    def mark_as_confirmed(self, request, queryset):
        rows = queryset.update(order_status=Order.STATUS_CONFIRMED)
        self.message_user(request, f"{rows} orders marked as Confirmed.")

    @admin.action(description="Mark selected orders as Processing")
    def mark_as_processing(self, request, queryset):
        rows = queryset.update(order_status=Order.STATUS_PROCESSING)
        self.message_user(request, f"{rows} orders marked as Processing.")

    @admin.action(description="Mark selected orders as Shipped")
    def mark_as_shipped(self, request, queryset):
        rows = queryset.update(order_status=Order.STATUS_SHIPPED)
        self.message_user(request, f"{rows} orders marked as Shipped.")

    @admin.action(description="Mark selected orders as Delivered")
    def mark_as_delivered(self, request, queryset):
        rows = queryset.update(order_status=Order.STATUS_DELIVERED, payment_status=Order.PAYMENT_STATUS_PAID)
        self.message_user(request, f"{rows} orders marked as Delivered & Paid.")

    @admin.action(description="Mark selected orders as Paid")
    def mark_as_paid(self, request, queryset):
        rows = queryset.update(payment_status=Order.PAYMENT_STATUS_PAID)
        self.message_user(request, f"{rows} orders marked as Paid.")


@admin.register(NewsletterSubscriber)
class NewsletterSubscriberAdmin(admin.ModelAdmin):
    list_display = ['email', 'subscribed_at']
    search_fields = ['email']
    ordering = ['-subscribed_at']
