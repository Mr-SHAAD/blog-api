# 📝 Blog API

A production-ready **REST API** for a blogging platform built with **Django REST Framework** and **PostgreSQL**.

[![Python](https://img.shields.io/badge/Python-3.11-blue?style=flat&logo=python)](https://python.org)
[![Django](https://img.shields.io/badge/Django-4.2-green?style=flat&logo=django)](https://djangoproject.com)
[![DRF](https://img.shields.io/badge/DRF-3.14-red?style=flat)](https://django-rest-framework.org)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-blue?style=flat&logo=postgresql)](https://postgresql.org)
[![JWT](https://img.shields.io/badge/Auth-JWT-orange?style=flat)](https://jwt.io)

---

## 🚀 Features

- ✅ **JWT Authentication** — Secure Register, Login, Token Refresh
- ✅ **Posts** — Full CRUD with author-only edit/delete protection
- ✅ **Comments** — Nested comments on posts
- ✅ **Like System** — Toggle like/unlike on posts
- ✅ **Role-based Access** — Only authors can modify their content
- ✅ **PostgreSQL** — Production-grade database
- ✅ **RESTful Design** — Clean, consistent API endpoints

---

## 🛠️ Tech Stack

| Technology | Usage |
|------------|-------|
| Python 3.11 | Core Language |
| Django 4.2 | Web Framework |
| Django REST Framework | API Development |
| PostgreSQL | Database |
| SimpleJWT | Authentication |
| python-decouple | Environment Variables |

---

## 📁 Project Structure

```
blog-api/
├── blog/
│   ├── models.py        # Post, Comment, Like models
│   ├── serializers.py   # Data serialization
│   ├── views.py         # API logic
│   └── urls.py          # URL routing
├── core1/
│   ├── settings.py      # Project settings
│   └── urls.py          # Main URLs
├── .gitignore
├── manage.py
└── README.md
```

---
## 🌐 Live Demo
https://blog-api-production-b09d.up.railway.app

## 🔗 API Endpoints

### Authentication
| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| POST | `/api/register/` | Register new user | ❌ |
| POST | `/api/login/` | Login — returns JWT token | ❌ |
| POST | `/api/token/refresh/` | Refresh access token | ❌ |

### Posts
| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| GET | `/api/posts/` | Get all posts | ✅ |
| POST | `/api/posts/` | Create new post | ✅ |
| GET | `/api/posts/{id}/` | Get post detail | ✅ |
| PUT | `/api/posts/{id}/` | Update post (author only) | ✅ |
| DELETE | `/api/posts/{id}/` | Delete post (author only) | ✅ |

### Comments & Likes
| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| POST | `/api/posts/{id}/comment/` | Add comment | ✅ |
| POST | `/api/posts/{id}/like/` | Toggle like/unlike | ✅ |

---

## ⚙️ Local Setup

### Prerequisites
- Python 3.11+
- PostgreSQL
- pip

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/Mr-SHAAD/blog-api.git
cd blog-api/core1

# 2. Create virtual environment
python -m venv env
source env/bin/activate  # Mac/Linux
env\Scripts\activate     # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Create .env file
touch .env
```

Add these to `.env`:
```
SECRET_KEY=your_secret_key
DEBUG=True
DB_NAME=blogapi
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```

```bash
# 5. Run migrations
python manage.py migrate

# 6. Create superuser
python manage.py createsuperuser

# 7. Run server
python manage.py runserver
```

---

## 🧪 Testing with Postman

**Step 1 — Register:**
```json
POST /api/register/
{
    "username": "testuser",
    "email": "test@gmail.com",
    "password": "pass123"
}
```

**Step 2 — Login:**
```json
POST /api/login/
{
    "username": "testuser",
    "password": "pass123"
}
```

**Step 3 — Use Token:**
```
Headers:
Authorization: Bearer <access_token>
```

---

## 👨‍💻 Author

**iamshaadgour**
- GitHub: [@Mr-SHAAD](https://github.com/Mr-SHAAD)
- LinkedIn: [Mohammad Shaad](https://linkedin.com/in/mohammad-shaad-672334204)
- Email: knowmore8126@gmail.com

---

⭐ **Star this repo if you found it helpful!**
