# NovaMart — Full-Stack E-Commerce Platform

A production-ready, responsive, full-stack e-commerce web application built with **Python**, **Django**, **Bootstrap 5**, **JavaScript**, and **SQLite/PostgreSQL**. Designed with modern aesthetics, robust inventory management, session-based cart operations, order snapshots, Cash on Delivery (COD) workflows, and comprehensive automated test coverage.

---

## 🌟 Key Features

### 🛒 Customer Storefront & Catalog
- **Dynamic Homepage**: Features hero banner promotions, shop-by-category cards, curated featured products, new arrivals, best sellers calculated from real order data, and a working newsletter subscription.
- **Product Catalog (`/products/`)**:
  - Live full-text search across product titles, descriptions, and category names.
  - Multi-attribute filtering: Category, Price range (Min / Max in ₹), and In-Stock availability.
  - Multi-criteria sorting: Newest arrivals, Price (Low to High), Price (High to Low), and Name (A–Z).
  - Server-side pagination preserving all active filter parameters.
- **Product Details (`/products/<slug>/`)**:
  - Image gallery with local high-resolution media fallbacks.
  - Real-time stock status badge (*In Stock*, *Low Stock Warning*, or *Out of Stock*).
  - Client-side and server-side validated quantity stepper preventing negative, zero, or stock-exceeding quantities.
  - Related product recommendations from the same department.

### 🛍️ Session-Based Shopping Cart (`/cart/`)
- Dynamic cart operations: Add, Increase, Decrease, Update quantity, and Remove item.
- Interactive AJAX updates for seamless quantity adjustments without page reload.
- Strict server-side stock validation: users cannot add or update to exceed current database inventory.
- Server-side monetary computations using Python's `Decimal` type to prevent floating-point rounding errors.
- Free Express Delivery milestone indicator (Orders above ₹999 qualify for Free Shipping).
- Persistent navbar cart counter badge across page navigation.

### 📦 Checkout & Atomic Order Processing (`/checkout/`)
- Requires customer authentication; pre-fills delivery details from account profile.
- Server-side re-verification of product prices and stock availability within a `transaction.atomic()` block.
- Automatic inventory reduction upon order confirmation.
- **OrderItem Snapshots**: Saves `product_name` and `unit_price` at the exact moment of purchase, preserving accounting records even if product prices or names change later.
- Session cart cleared automatically after successful transaction.
- **Cash on Delivery (COD)** payment method supported with zero advance payment risk.
- Prevention of duplicate order submissions via frontend button locking and server tokens.

### 📜 Order Tracking & History (`/orders/`)
- **Order Confirmation (`/orders/<order_number>/`)**: Instant display of unique order reference number (e.g., `ORD-20261022-A1B2C3D4`) and item breakdown.
- **My Orders (`/orders/`)**: Complete order history showing order numbers, placement dates, total amounts, and status badges.
- **Order Details (`/orders/<order_number>/details/`)**:
  - Visual tracking progress stepper (*Pending* → *Confirmed* → *Processing* → *Shipped* → *Delivered*).
  - Strict privacy protections: customers can only view their own orders.
  - **Self-Service Order Cancellation**: Customers can cancel orders in *Pending* or *Confirmed* status; items are atomically returned to inventory.

### 👤 Authentication & User Profiles (`/accounts/`)
- Secure registration with full name, username, email, and password strength checks.
- Flexible login: users can authenticate using either their **Username OR Email Address**.
- User profile dashboard (`/account/`) with profile editing and recent order activity stats.
- Passwords hashed using Django's PBKDF2 with SHA-256 (no plaintext storage).

### 🛡️ Administrative Portal (`/admin/`)
- Custom Django Admin configurations for `Product`, `Category`, `Order`, `OrderItem`, and `NewsletterSubscriber`.
- Inline order items, image thumbnail previews, stock availability badges, and search filters.
- Batch actions for updating order statuses (*Mark as Confirmed*, *Processing*, *Shipped*, *Delivered & Paid*).
- Staff-only access enforcement.

---

## 🛠️ Technology Stack

| Layer | Technology |
|---|---|
| **Backend Framework** | Python 3.13, Django 6.1 |
| **Database** | SQLite (Development) / PostgreSQL (Production ready) |
| **Frontend Styling** | Custom CSS3 design system + Bootstrap 5.3 + Bootstrap Icons |
| **Typography** | Google Fonts (*Plus Jakarta Sans* & *Outfit*) |
| **JavaScript** | Vanilla JS + Fetch API (AJAX cart updates & notifications) |
| **Image Processing** | Pillow (PIL) |
| **Environment Management** | `python-dotenv` |

---

## 📁 Project Directory Structure

```
ecommerce_project/
├── manage.py
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
│
├── ecommerce_project/
│   ├── __init__.py
│   ├── settings.py          # App settings, DB config, auth backends, static/media
│   ├── urls.py              # Root URL routing and custom error handlers
│   ├── wsgi.py
│   └── asgi.py
│
├── shop/
│   ├── migrations/          # Database migrations
│   ├── templates/
│   │   └── shop/
│   │       ├── base.html              # Foundation layout, navbar, footer, toasts
│   │       ├── home.html              # Hero, categories, featured, best sellers
│   │       ├── product_list.html      # Catalog with search, filters, pagination
│   │       ├── product_detail.html    # Product detail, stock badges, related items
│   │       ├── category_list.html     # All categories department listing
│   │       ├── cart.html              # Responsive cart table & summary card
│   │       ├── checkout.html          # Delivery address & COD payment
│   │       ├── order_confirmation.html# Thank-you page with order number & tracker
│   │       ├── order_list.html        # Customer order history
│   │       ├── order_detail.html      # Order detail, tracking stepper, cancel modal
│   │       ├── account.html           # User profile & order statistics
│   │       ├── register.html          # Account registration form
│   │       ├── login.html             # Login with username or email
│   │       ├── 404.html               # Custom 404 page
│   │       └── 500.html               # Custom 500 page
│   ├── static/
│   │   └── shop/
│   │       ├── css/style.css          # Design system tokens, cards, buttons, steppers
│   │       ├── js/main.js             # AJAX cart operations, steppers, toasts
│   │       └── images/placeholder.svg # Fallback SVG image
│   ├── models.py            # Category, Product, Order, OrderItem, NewsletterSubscriber
│   ├── views.py             # View controllers and business logic
│   ├── urls.py              # Namespaced shop URL patterns
│   ├── forms.py             # Form classes with validations
│   ├── cart.py              # Session cart manager with Decimal computation
│   ├── backends.py          # Custom Email or Username authentication backend
│   ├── context_processors.py# Global cart count, categories, and currency
│   ├── admin.py             # Django admin customizations and actions
│   ├── tests.py             # Comprehensive automated test suite
│   └── management/
│       └── commands/
│           └── load_sample_data.py # Sample data seeder generating 16 products & images
│
└── media/
    └── products/            # Uploaded and seeded product images
```

---

## 🚀 Quick Setup & Execution Guide (VS Code / Terminal)

Follow these step-by-step instructions to get the application running on your computer.

### Step 1: Open the Project Directory
Open the project directory in Visual Studio Code or your command terminal:
```bash
cd "c:\Users\user\Documents\code alpha project"
```

### Step 2: Create & Activate Virtual Environment
**On Windows:**
```powershell
python -m venv venv
venv\Scripts\activate
```

**On macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Required Dependencies
```bash
python -m pip install -r requirements.txt
```

### Step 4: Run Database Migrations
Create the SQLite database and create all tables:
```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 5: Seed Sample Products & Categories
Populate the store with 16 realistic demo products across 5 categories with locally rendered images:
```bash
python manage.py load_sample_data
```

### Step 6: Create an Administrator Account
Create a staff account to access the administrative dashboard:
```bash
python manage.py createsuperuser
```
*(Or use the pre-created demo admin credentials: Username: `admin`, Password: `Admin@12345`)*

### Step 7: Launch the Development Server
```bash
python manage.py runserver
```

### Step 8: Open in Your Browser
- **Customer Storefront**: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- **Django Admin Portal**: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## 🧪 Running Automated Tests

Run the full automated test suite covering authentication, catalog, cart logic, stock validation, checkout, atomic inventory decrements, order cancellation, and permission checks:

```bash
python manage.py test
```

Expected output:
```
Ran 22 tests in 10.969s

OK
```

---

## 🛡️ Security Implementation

- **CSRF Protection**: All POST requests (forms and AJAX) include cross-site request forgery validation tokens.
- **Safe SQL / ORM Queries**: All database interactions use the Django ORM to prevent SQL injection vulnerabilities.
- **Strict Monetary Precision**: All calculations use Python's `Decimal` type via `DecimalField`, avoiding floating-point imprecision.
- **Secure Password Hashing**: Utilizes PBKDF2 with SHA-256 hashing; plain-text passwords are never stored.
- **Role-Based Access Control**: Regular customers cannot view or modify other users' orders or access administrative endpoints.
- **Atomic Transactions**: Orders and stock changes are wrapped inside `transaction.atomic()` to prevent partial saves or race conditions.

---

## 🌐 Production Deployment Considerations

1. **Environment Variables**: Copy `.env.example` to `.env` and set a unique `SECRET_KEY`, `DEBUG=False`, and appropriate `ALLOWED_HOSTS`.
2. **PostgreSQL Migration**: Set `DB_ENGINE=django.db.backends.postgresql` and provide database credentials in `.env`.
3. **Static & Media Files**: Run `python manage.py collectstatic` and configure a reverse proxy (e.g., Nginx) or cloud storage (AWS S3, Cloudinary) to serve `/static/` and `/media/`.
4. **Payment Gateway Integration**: Ready for Razorpay or Stripe by adding the webhook handler in `shop/views.py`.
