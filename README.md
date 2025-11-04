# 💳 ApplyPay

ApplyPay is a **full-stack web application** built with **FastAPI (backend)** and **React (frontend)**.  
It allows users to submit application forms and make secure payments via **Razorpay**.  
The backend is powered by **FastAPI**, **MySQL**, **Celery**, and **Redis**, and the frontend is built using **React** with responsive UI components.

---

## 🚀 Features

### 🖥️ Frontend (React)
- Responsive user interface for the application form and payment flow  
- Integration with Razorpay Checkout  
- API communication with FastAPI backend  
- Form validation and success/error handling  

### ⚙️ Backend (FastAPI)
- RESTful APIs for managing user applications and payments  
- Razorpay payment integration  
- Asynchronous task processing with Celery + Redis  
- Database management using SQLAlchemy + MySQL  
- Dockerized for scalable deployment  

---

## 🧱 Tech Stack

| Layer | Technology |
|-------|-------------|
| Frontend | React |
| Backend | FastAPI, Python 3.11 |
| Database | MySQL |
| Task Queue | Celery + Redis |
| Payments | Razorpay |
| Containerization | Docker & Docker Compose |

---

## 🛠️ Setup Instructions

### 1️⃣ Clone the repository
```bash
git clone git@github.com:AkshayaBenny/ApplyPay.git
cd ApplyPay
