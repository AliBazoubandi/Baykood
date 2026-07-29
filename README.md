# Baykood — فروشگاه کشاورزی آنلاین بایکود

A full-featured Persian (RTL) agriculture e-commerce website built with Django and Tailwind CSS.

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-5.x-green?logo=django&logoColor=white)
![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-v4-38BDF8?logo=tailwindcss&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-336791?logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Compose-2496ED?logo=docker&logoColor=white)

---

## ✨ Features

- 🛒 **Full shop** — product catalog, categories, product detail with image gallery
- 🛍️ **Cart & checkout** — session-based cart, order placement with address form
- 📦 **Order management** — order history in user profile, admin order tracking with status badges
- 📝 **Blog** — post list with tag filtering, YouTube & Instagram video embeds
- 👤 **User accounts** — register, login, profile, order history
- 🔧 **Django Admin** — fully Persian admin panel with image previews and inline order items
- 📱 **Mobile-first** — responsive design with hamburger menu
- 🌿 **Earthy & rustic design** — custom Tailwind color palette, Vazirmatn Persian font
- 📡 **SEO ready** — sitemap.xml, robots.txt
- 💬 **Telegram integration** — contact button throughout the site
- 🇮🇷 **Full RTL support** — Persian language, right-to-left layout

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Backend | Django 5.x |
| Database | PostgreSQL 16 (Docker) |
| Frontend | Tailwind CSS v4 |
| Icons | Lucide Icons |
| Font | Vazirmatn |
| Containerization | Docker Compose |

---

## 🚀 Getting Started

### Prerequisites

Make sure you have these installed:

- Python 3.10+
- Node.js LTS
- Docker Desktop

### 1 — Clone the repository

```bash
git clone https://github.com/AliBazoubandi/Baykood
cd agrishop
```

### 2 — Create and activate virtual environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac / Linux
source venv/bin/activate
```

### 3 — Install Python dependencies

```bash
pip install -r requirements.txt
```

### 4 — Install Node dependencies (for Tailwind)

```bash
npm install
```

### 5 — Set up environment variables

Create a `.env` file in the root directory:

```env
SECRET_KEY=your-secret-key-here
DEBUG=True
DB_NAME=agrishop_db
DB_USER=agrishop_user
DB_PASSWORD=yourpassword123
DB_HOST=localhost
DB_PORT=5432
```

### 6 — Start the database

```bash
docker compose up -d
```

### 7 — Run migrations

```bash
python manage.py migrate
```

### 8 — Create a superuser

```bash
python manage.py createsuperuser
```

### 9 — Start Tailwind (Terminal 1)

```bash
npx @tailwindcss/cli -i ./static/css/input.css -o ./static/css/output.css --watch --content "./templates/**/*.html"
```

### 10 — Start Django (Terminal 2)

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` — the site is running.
Admin panel: `http://127.0.0.1:8000/admin/`

---

## 📁 Project Structure

```bash
Baykood-main/
├── agrishop/               # Django project config
│   ├── settings.py
│   ├── urls.py
│   └── admin_config.py
├── apps/
│   ├── shop/               # Products, categories, cart, orders
│   ├── blog/               # Posts, tags, video embeds
│   ├── accounts/           # User auth, profile
│   └── core/               # Homepage, about, contact, sitemaps
├── templates/              # All HTML templates
│   ├── base.html
│   ├── core/
│   ├── shop/
│   ├── blog/
│   └── accounts/
├── static/
│   └── css/input.css       # Tailwind source
├── media/                  # Uploaded images (gitignored)
├── docker-compose.yml
├── requirements.txt
└── .env                    # Not committed — see .env example above

```

## 🔧 Admin Panel

Access the Django admin at `/admin/` with your superuser credentials.

From the admin you can:
- Add / edit products and categories with image upload
- Write and publish blog posts with video embed links
- View and manage customer orders with status tracking
- Read contact form submissions
- Manage user accounts

---

## 📱 Screenshots

> Add screenshots here after deployment

---

## 🗺️ Roadmap

- [ ] Payment gateway integration (Zarinpal / IDPay)
- [ ] Product search
- [ ] Pagination
- [ ] Deployment (Gunicorn + Nginx)

---

## 📄 License

This project is for portfolio and educational purposes.

---

Built with ❤️ using Django & Tailwind CSS