import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import django
import requests
from PIL import Image

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce_project.settings')
django.setup()

from django.conf import settings
from shop.models import Product, Category, Order, OrderItem

report_lines = []
report_lines.append("# NovaMart Comprehensive Product Catalogue & Image Audit Report")
report_lines.append("\n## Executive Summary")

total_products = Product.objects.count()
active_products = Product.objects.filter(is_active=True).count()
total_categories = Category.objects.count()

missing_images = 0
unreadable_images = 0
format_mismatches = 0
unmatched_categories = 0
verified_count = 0

report_lines.append(f"- **Total Products Audited**: {total_products}")
report_lines.append(f"- **Active Products**: {active_products}")
report_lines.append(f"- **Total Departments/Categories**: {total_categories}")

details_table = []
details_table.append("| ID | Product Name | Category | Image Filename | Exists | Openable | Format | Status |")
details_table.append("|:---:|---|---|---|:---:|:---:|:---:|:---:|")

for product in Product.objects.all().order_by('id'):
    rel_path = str(product.image)
    abs_path = os.path.join(settings.MEDIA_ROOT, rel_path)
    filename = os.path.basename(rel_path)
    
    file_exists = os.path.exists(abs_path)
    can_open = False
    img_format = "N/A"
    status = "VERIFIED"
    
    if not file_exists:
        missing_images += 1
        status = "MISSING_FILE"
    else:
        try:
            with Image.open(abs_path) as im:
                can_open = True
                img_format = im.format # e.g. JPEG
                # Check format matches extension
                if filename.lower().endswith(('.jpg', '.jpeg')) and img_format != 'JPEG':
                    format_mismatches += 1
                    status = "FORMAT_MISMATCH"
                elif filename.lower().endswith('.png') and img_format != 'PNG':
                    format_mismatches += 1
                    status = "FORMAT_MISMATCH"
        except Exception:
            unreadable_images += 1
            status = "UNREADABLE"

    if status == "VERIFIED":
        verified_count += 1

    details_table.append(f"| {product.id} | {product.name} | {product.category.name} | `{filename}` | {'Yes' if file_exists else 'No'} | {'Yes' if can_open else 'No'} | {img_format} | **{status}** |")

report_lines.append(f"- **Verified Correct & Intact Images**: {verified_count}/{total_products} ({(verified_count/total_products)*100:.1f}%)")
report_lines.append(f"- **Missing Image Files**: {missing_images}")
report_lines.append(f"- **Corrupt/Unreadable Images**: {unreadable_images}")
report_lines.append(f"- **Format Mismatches**: {format_mismatches}")

report_lines.append("\n## Audit Details per Product")
report_lines.extend(details_table)

artifact_path = r"C:\Users\user\.gemini\antigravity-ide\brain\720768eb-cf1a-4477-89a6-7db5e3cb7cd4\catalog_verification_report.md"
os.makedirs(os.path.dirname(artifact_path), exist_ok=True)
with open(artifact_path, "w", encoding="utf-8") as f:
    f.write("\n".join(report_lines))

print(f"Audit completed: {verified_count}/{total_products} products verified!")
print(f"Report written to {artifact_path}")
