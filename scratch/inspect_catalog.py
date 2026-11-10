import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import django
import hashlib

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce_project.settings')
django.setup()

from django.conf import settings
from shop.models import Product, Category, Order, OrderItem

print("="*60)
print("CATALOGUE & MEDIA DIAGNOSTIC REPORT")
print("="*60)

total_products = Product.objects.count()
total_categories = Category.objects.count()
total_orders = Order.objects.count()
total_order_items = OrderItem.objects.count()

print(f"Total Products: {total_products}")
print(f"Total Categories: {total_categories}")
print(f"Total Orders: {total_orders}")
print(f"Total Order Items: {total_order_items}")

hashes = {}
missing_files = []
unreadable_files = []

for p in Product.objects.all():
    image_rel = str(p.image)
    image_abs = os.path.join(settings.MEDIA_ROOT, image_rel)
    
    if not os.path.exists(image_abs):
        missing_files.append((p.id, p.name, image_rel))
        continue
    
    try:
        data = open(image_abs, 'rb').read()
        file_hash = hashlib.md5(data).hexdigest()
        hashes.setdefault(file_hash, []).append((p.id, p.name, p.category.name, image_rel))
    except Exception as e:
        unreadable_files.append((p.id, p.name, str(e)))

print(f"\nMissing Image Files: {len(missing_files)}")
print(f"Unreadable Files: {len(unreadable_files)}")
print(f"Distinct Image Content Hashes: {len(hashes)} out of {total_products} products")

print("\n--- Image Hash Repetitions (Showing how identical images were assigned to unrelated products) ---")
for h, prods in list(hashes.items())[:5]:
    print(f"\nHash {h[:8]} is shared by {len(prods)} products:")
    for pid, pname, cat, img in prods[:4]:
        print(f"  [ID {pid}] ({cat}) {pname} -> {img}")
    if len(prods) > 4:
        print(f"  ... and {len(prods) - 4} more products sharing this exact same image!")

print("\n" + "="*60)
