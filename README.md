# 🌱 بایکود (Baykood)

A full-featured Persian (RTL) agriculture e-commerce website built with Django, Tailwind CSS v4, and PostgreSQL — fully Dockerized and production-ready.

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-6.x-green?logo=django&logoColor=white)
![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-v4-38BDF8?logo=tailwindcss&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-18-336791?logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Compose-2496ED?logo=docker&logoColor=white)

---

## ✨ Features

### 🛒 Shop
- Product catalog with categories, image galleries, and stock tracking
- Low-stock warning badges ("فقط ۳ عدد باقی‌مانده")
- Session-based cart — add, update, remove
- Full checkout flow with address form → order creation
- Order confirmation page + order history in user profile
- Product search across products and blog posts
- Pagination on product and blog listings

### 📝 Blog
- Post list with tag filtering
- Automatic YouTube & Instagram video embedding from a pasted URL
- Related posts

### 👤 Accounts
- Register, login, logout
- Profile page with avatar, phone, address
- Order history with live status badges

### 🎨 Design
- Fully RTL, Persian-first UI
- Custom Mikhak variable font (self-hosted, no external font requests)
- Earthy & rustic color palette built with Tailwind v4 `@theme`
- Mobile-first responsive layout with hamburger navigation
- Smooth custom-duration scroll animations + scroll-to-top button
- Floating Telegram contact button
- Dynamic homepage category strip — fully driven from the admin panel, supports both Lucide icons and custom uploaded icon images (e.g. Flaticon)

### 🔧 Admin (Django Admin, fully in Persian)
- Product, category, blog, and order management with image previews
- Inline order items with live subtotal calculation
- Order status tracking with color-coded badges
- Contact form submissions inbox

### 📡 SEO & Discoverability
- `sitemap.xml` (auto-generated from products, categories, posts)
- `robots.txt`
- Meta descriptions, Open Graph, and Twitter Card tags per page (product, blog post, category)
- Custom Persian 404 / 500 error pages

### 💬 Contact & Social
- Contact form saved to the database, readable from admin
- Telegram, Instagram, YouTube, WhatsApp, Rubika, Bale, and Soroush Plus links — all managed from a single config, shown consistently in the footer and contact page

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Backend | Django 6.x |
| Database | PostgreSQL 18 |
| Frontend | Tailwind CSS v4 |
| Icons | Lucide Icons + custom uploaded icons |
| Font | Mikhak (self-hosted variable font) |
| Production server | Gunicorn |
| Static files | Whitenoise |
| Containerization | Docker Compose |

---

## 🚀 Getting Started (Docker — recommended)

### Prerequisites
- Docker Desktop

### 1 — Clone the repository

```bash
git clone https://github.com/AliBazoubandi/Baykood.git
cd Baykood
```

### 2 — Set up environment variables

Create a `.env` file in the root directory:

```env
SECRET_KEY=your-secret-key-here
DEBUG=True
DB_NAME=agrishop_db
DB_USER=agrishop_user
DB_PASSWORD=yourpassword123
DB_HOST=db
DB_PORT=5432
```

### 3 — Build the Tailwind CSS once before building the image

```bash
npx @tailwindcss/cli -i ./tailwind/input.css -o ./static/css/output.css --minify
```

### 4 — Build and start everything

```bash
docker compose up -d --build
```

### 5 — Run migrations and create a superuser

```bash
docker compose exec web python manage.py migrate
docker compose exec web python manage.py createsuperuser
```

Visit `http://localhost:8000` — the site is running.
Admin panel: `http://localhost:8000/admin/`

---

## 🧑‍💻 Getting Started (Local, without Docker)

### Prerequisites
- Python 3.12+
- Node.js LTS
- Docker Desktop (for PostgreSQL only)

### 1 — Create and activate a virtual environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac / Linux
source venv/bin/activate
```

### 2 — Install dependencies

```bash
pip install -r requirements.txt
npm install
```

### 3 — Set `.env` for local development

```env
SECRET_KEY=your-secret-key-here
DEBUG=True
DB_NAME=agrishop_db
DB_USER=agrishop_user
DB_PASSWORD=yourpassword123
DB_HOST=localhost
DB_PORT=5432
```

### 4 — Start PostgreSQL only

```bash
docker compose up -d db
```

### 5 — Run migrations and create a superuser

```bash
python manage.py migrate
python manage.py createsuperuser
```

### 6 — Start Tailwind (Terminal 1)

```bash
npx @tailwindcss/cli -i ./tailwind/input.css -o ./static/css/output.css --watch --content "./templates/**/*.html"
```

### 7 — Start Django (Terminal 2)

```bash
python manage.py runserver
```

---

## 📁 Project Structure

```bash
Baykood/
├── agrishop/ # Django project config
│ ├── settings.py
│ ├── urls.py
│ └── admin_config.py
├── shop/ # Products, categories, cart, orders
├── blog/ # Posts, tags, video embeds
├── accounts/ # User auth, profile
├── core/ # Homepage, about, contact, sitemaps
├── templates/
│ ├── base.html
│ ├── partials/ # Reusable includes (social links, pagination)
│ ├── core/ shop/ blog/ accounts/
│ ├── 404.html / 500.html / robots.txt
├── tailwind/
│ └── input.css # Tailwind v4 source (theme, fonts)
├── static/
│ ├── css/output.css # Compiled Tailwind output
│ ├── fonts/ # Mikhak variable font
│ ├── favicon/
│ └── icons/social/ # Rubika, Bale, Soroush icons
├── media/ # Uploaded images (gitignored)
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── .env # Not committed

```

---

## 🔧 Admin Panel

From `/admin/` you can:
- Add/edit products and categories — including custom category icons and homepage display order
- Write and publish blog posts with video embed links
- Manage customer orders with status tracking
- Read contact form submissions
- Manage user accounts

---

## 🗺️ Roadmap

- [ ] Persian (Jalali) date display
- [ ] Blog post reading time
- [ ] Admin dashboard stats (orders, revenue, low stock at a glance)
- [ ] Image optimization/compression on upload
- [ ] Payment gateway integration (Zarinpal / IDPay)
- [ ] Production deployment (domain + server + HTTPS)

---

## 📄 License

This project is for portfolio and educational purposes.

---

Built with ❤️ using Django, Tailwind CSS, and a lot of trial and error.