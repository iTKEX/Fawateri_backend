# ⚙️ Fawateri

**Fawateri** is a smart and secure invoice management application that allows users to store, organize, and access all types of invoices in one place, including purchase receipts, car maintenance bills, and device repair invoices.
It helps users easily retrieve invoices when needed, especially for warranty claims or service follow-ups.

---

## 📘 Project Description

The **Fawateri Backend** is built using **Django 5** and **Django REST Framework (DRF)**.  
It serves as the core logic and data layer, offering endpoints for authentication, bill CRUD operations, reminders, and categorization.  
The backend also integrates **JWT authentication** and supports **receipt image uploads** for each bill.

---

### 🔹 Main Features
- User registration and login via JWT authentication  
- Bill management (create, read, update, delete)  
- Upload and manage receipt images  
- Categorize bills by type  
- Create reminders for payments or warranty expiration  
- Filter bills by category or date  

> Designed for individual users — no admin roles are included.

---

## 🧩 Tech Stack

| Category | Technology |
|-----------|-------------|
| **Language** | Python |
| **Framework** | Django 5 |
| **API Toolkit** | Django REST Framework |
| **Authentication** | JWT (SimpleJWT) |
| **Database** | PostgreSQL |

---

## 🔗 Related Repository

[**Fawateri Frontend**](https://github.com/iTKEX/Fawateri_frontend)

---

## 🌐 Live Link

[**Backend**](http://localhost:8000)

---

## 🗺️ Entity Relationship Diagram (ERD)

![ERD](./assets/Fawateri-ERD.svg)

---

## 🧭 Routing Table

### 🧑‍💻 Users
| HTTP Method | Path | Description |
|--------------|------|--------------|
| **POST** | `/users/signup/` | Create a new user account |
| **GET** | `/users/login/` | Log in to an existing account |
| **POST** | `/users/verify/` | Verify user credentials and permissions |

---

### 💳 Bills
| HTTP Method | Path | Description |
|--------------|------|--------------|
| **GET** | `/bills/` | List all bills |
| **GET** | `/bills/{bill_id}/` | Show details of a bill |
| **POST** | `/bills/` | Create a new bill |
| **PUT** | `/bills/{bill_id}/` | Update bill details |
| **DELETE** | `/bills/{bill_id}/` | Delete a bill |

---

### 🗂️ Categories
| HTTP Method | Path | Description |
|--------------|------|--------------|
| **GET** | `/categories/` | List all categories |
| **DELETE** | `/categories/{id}/` | Delete a category |

---

### ⏰ Reminders
| HTTP Method | Path | Description |
|--------------|------|--------------|
| **GET** | `/bills/{bill_id}/reminders/` | List all reminders for a bill |
| **POST** | `/bills/{bill_id}/reminders/` | Create a new reminder for a bill |
| **DELETE** | `/bills/{bill_id}/reminders/{reminder_id}/` | Delete a reminder |

---

### 🖼️ Images
| HTTP Method | Path | Description |
|--------------|------|--------------|
| **GET** | `/bills/{bill_id}/image/` | Get the bill image |
| **POST** | `/bills/{bill_id}/image/` | Add a new image to a bill |
| **DELETE** | `/image/{image_id}/` | Delete an image |

---

### 🔗 Bills & Categories (M:M Relationship)
| HTTP Method | Path | Description |
|--------------|------|--------------|
| **GET** | `/bills/{bill_id}/categories/` | List categories linked to a bill |
| **POST** | `/bills/{bill_id}/categories/{category_id}/` | Attach a category to a bill |
| **DELETE** | `/bills/{bill_id}/categories/{category_id}/` | Remove a category from a bill |

---

## 🚀 Installation & Running the Project

You can run the **Fawateri Backend** in two ways:  
**(1) Locally (via Python & Pipenv)** or **(2) using Docker Compose**.

---

### 🧱 1. Run Locally

#### Prerequisites
- Python 3.11+  
- PostgreSQL (or SQLite for local testing)  
- Pipenv (optional but recommended)

#### Steps
```bash
# Clone the repository
git clone https://github.com/iTKEX/Fawateri_backend
cd Fawateri_backend
```
```bash
# Create a virtual environment
pipenv shell
```
```bash
# Install dependencies
pip install -r requirements.txt
```
```bash
# Set up the database (make sure DB config in settings.py is correct)
python manage.py migrate
```
```bash
# Create a superuser (optional)
python manage.py createsuperuser
```
```bash
# Run the development server
python manage.py runserver
```

Then open your browser at:  
👉 [http://localhost:8000](http://localhost:8000)

---

### 🐳 2. Run Using Docker

#### Steps
```bash
# Clone the repository
git clone https://github.com/iTKEX/Fawateri_backend
```
```bash
# Build and start the containers
docker-compose up
```

Once started, the app will be available at:  
👉 [http://localhost:8000](http://localhost:8000)

---

## 🧊 IceBox Features (Planned Enhancements)

- **📱 Mobile App API Support:**  
  Dedicated mobile-friendly API layer optimized for iOS/Android clients (light payloads, versioned endpoints).

- **🤖 OCR Data Extraction:**  
  Auto-extract amount, date, and merchant details from uploaded receipt images.

- **📨 Email Notifications:**  
  Scheduled/background notifications for bill due dates and warranty expirations (Celery + Redis).

- **📈 Spending Analytics API:**  
  Endpoints for monthly totals, category breakdowns, and trends for frontend dashboards.

- **☁️ Cloud File Storage:**  
  Store attachments on AWS S3 or Google Cloud Storage with signed URLs and lifecycle rules.

- **🔒 Security & Compliance:**  
  At-rest encryption, API rate limiting, and caching via Redis for performance and protection.
