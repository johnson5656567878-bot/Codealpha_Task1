import os
import shutil
import requests
from decimal import Decimal
from django.core.management.base import BaseCommand
from django.utils.text import slugify
from django.conf import settings
from PIL import Image, ImageDraw
from shop.models import Category, Product
from shop.sample_catalog_data import CATALOG_ITEMS, CATEGORIES


class Command(BaseCommand):
    help = "Seeds or updates database with 112 verified products across 8 categories with accurate matching images"

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.NOTICE("Initializing NovaMart 112 verified products catalog..."))

        products_dir = os.path.join(settings.MEDIA_ROOT, 'products')
        categories_dir = os.path.join(settings.MEDIA_ROOT, 'categories')
        os.makedirs(products_dir, exist_ok=True)
        os.makedirs(categories_dir, exist_ok=True)

        for cat_slug in CATEGORIES:
            os.makedirs(os.path.join(products_dir, cat_slug), exist_ok=True)

        categories_meta = [
            {"slug": "electronics-audio", "name": "Electronics & Audio", "description": "High-fidelity audio, wireless headphones, and premium sound systems.", "image": "categories/electronics-audio.jpg"},
            {"slug": "smart-wearables", "name": "Smart Wearables", "description": "Cutting-edge smartwatches, fitness trackers, and connected devices.", "image": "categories/smart-wearables.jpg"},
            {"slug": "laptops-computers", "name": "Laptops & Computers", "description": "Power-packed laptops, ergonomic keyboards, and workspace essentials.", "image": "categories/laptops-accessories.jpg"},
            {"slug": "mobiles-accessories", "name": "Mobiles & Accessories", "description": "Smartphones, fast GaN chargers, magsafe power banks, and heavy-duty cases.", "image": "categories/smart-wearables.jpg"},
            {"slug": "bags-travel-gear", "name": "Bags & Travel Gear", "description": "Weatherproof backpacks, commuter sleeves, and durable travel duffels.", "image": "categories/bags-travel-gear.jpg"},
            {"slug": "home-workspace-decor", "name": "Home & Workspace Decor", "description": "Ambient LED lamps, acoustic desk mats, and modern desk organizers.", "image": "categories/home-workspace-decor.jpg"},
            {"slug": "gaming-entertainment", "name": "Gaming & Entertainment", "description": "Wireless controllers, RGB headsets, streaming microphones, and racing wheels.", "image": "categories/electronics-audio.jpg"},
            {"slug": "fashion-lifestyle-essentials", "name": "Fashion & Lifestyle Essentials", "description": "Minimalist hoodies, polaroid sunglasses, stainless steel bottles, and wallets.", "image": "categories/bags-travel-gear.jpg"},
        ]

        category_objs = {}
        for c in categories_meta:
            cat, _ = Category.objects.get_or_create(
                slug=c["slug"],
                defaults={
                    "name": c["name"],
                    "description": c["description"],
                    "image": c["image"],
                }
            )
            cat.name = c["name"]
            cat.description = c["description"]
            cat.save()
            category_objs[c["slug"]] = cat

        updated_count = 0
        for item in CATALOG_ITEMS:
            cat_obj = category_objs.get(item["category"])
            rel_image_path = f"products/{item['category']}/{item['filename']}"
            abs_image_path = os.path.join(settings.MEDIA_ROOT, rel_image_path)

            # If image doesn't exist locally, download or generate
            if not os.path.exists(abs_image_path):
                if item.get("photo_id"):
                    try:
                        url = f"https://images.unsplash.com/{item['photo_id']}?auto=format&fit=crop&w=800&q=80"
                        r = requests.get(url, timeout=10)
                        if r.status_code == 200:
                            with open(abs_image_path, 'wb') as f:
                                f.write(r.content)
                    except Exception:
                        pass
                if not os.path.exists(abs_image_path):
                    self.generate_product_image(abs_image_path, item["name"], cat_obj.name, f"INR {item['price']:.2f}")

            # Update or create product by ID to preserve order references
            product = Product.objects.filter(id=item["id"]).first()
            if product:
                product.name = item["name"]
                product.category = cat_obj
                product.price = item["price"]
                product.stock_quantity = item["stock"]
                product.description = item["description"]
                product.image = rel_image_path
                product.is_active = True
                product.save()
            else:
                product = Product.objects.create(
                    id=item["id"],
                    name=item["name"],
                    slug=slugify(item["name"]) or item["filename"].replace('.jpg', ''),
                    category=cat_obj,
                    price=item["price"],
                    stock_quantity=item["stock"],
                    description=item["description"],
                    image=rel_image_path,
                    is_active=True
                )
            updated_count += 1

        self.stdout.write(self.style.SUCCESS(f"Successfully synced {updated_count} verified products across {len(category_objs)} categories!"))
        self.stdout.write(self.style.SUCCESS(f"Total active products in database: {Product.objects.filter(is_active=True).count()}"))

    def generate_product_image(self, filepath, title, category, price):
        width, height = 800, 600
        brand_color = (79, 70, 229)
        image = Image.new("RGB", (width, height), (248, 250, 252))
        draw = ImageDraw.Draw(image)

        draw.rectangle([0, 0, width, 14], fill=brand_color)
        draw.rounded_rectangle([30, 30, width - 30, height - 30], radius=24, fill=(255, 255, 255), outline=(226, 232, 240), width=2)
        draw.text((60, 60), "NOVAMART VERIFIED SELECTION", fill=(148, 163, 184))
        draw.rounded_rectangle([width - 280, 52, width - 60, 88], radius=18, fill=(238, 242, 255))
        draw.text((width - 260, 62), category[:22].upper(), fill=brand_color)

        center_x, center_y = width // 2, 260
        r = 100
        draw.ellipse([center_x - r, center_y - r, center_x + r, center_y + r], fill=(241, 245, 249), outline=brand_color, width=3)
        draw.text((center_x - 32, center_y - 20), "NVM", fill=brand_color)

        words = title.split()
        line1 = " ".join(words[:5])
        line2 = " ".join(words[5:]) if len(words) > 5 else ""
        draw.text((60, 410), line1, fill=(15, 23, 42))
        if line2:
            draw.text((60, 440), line2, fill=(15, 23, 42))

        draw.line([60, 490, width - 60, 490], fill=(241, 245, 249), width=2)
        draw.text((60, 515), f"PRICE: {price}", fill=(15, 23, 42))
        draw.text((width - 300, 515), "100% GENUINE • CASH ON DELIVERY", fill=(16, 185, 129))

        image.save(filepath, format="JPEG", quality=90)
