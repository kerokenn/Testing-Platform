# Testing-PlatformV1
Wu and Co.


# Mock Testing Platform

A scalable, high-performance mock testing platform designed initially for the Civil Service Exam (CSE), with architectural flexibility to scale for the Licensure Examination for Teachers (LPT). Built with a security-first DevSecOps pipeline.

## 🏗️ Architecture & Tech Stack

This project utilizes a **Monorepo architecture** to streamline deployments and maintain strict type-safety and context across the stack.

### Core Development Stack
* **Frontend:** React + TypeScript (Hosted on Vercel)
* **Backend:** Python + FastAPI (Hosted on Render)
* **Database & Authentication:** Firebase (Firestore & Firebase Auth)

### DevSecOps & Security Stack
* **CI/CD:** GitHub Actions (Automated testing & deployment gates)
* **SCA & SAST:** Snyk / Dependabot / SonarCloud (Automated vulnerability scanning)
* **Secrets Management:** Doppler / HashiCorp Vault (No `.env` files committed to repo)
* **WAF:** Cloudflare (DDoS & bot mitigation)

---

# Installation Guide

# Back-end Installation
cd backend

python -m venv venv

.\venv\Scripts\activate

pip install fastapi

pip install "uvicorn[standard]"

pip install firebase-admin

pip install -r requirements.txt

---

# Front-end Installation

cd frontend

npm install

---

## 📁 Repository Structure

```text
mock-testing-platform/
│
├── FRONTEND (Vercel / React + TypeScript) 
│   │   # Responsible for UI, routing, and user experience
│   │
│   ├── Public Module
│   │   ├── Landing Page -----------------------> (Reads static/cached data)
│   │   └── Auth Pages (Login/Register) --------> Connects to: Firebase Auth
│   │
│   ├── Examinee Module
│   │   ├── Main Dashboard (Stats/History) -----> Connects to: User & Analytics Services
│   │   ├── Exam Catalog (Filters/Search) ------> Connects to: Exam Delivery Service
│   │   ├── Active Exam UI (Timer/Questions) ---> Connects to: Exam Delivery Service
│   │   └── Results & Review (Post-Exam) -------> Connects to: Grading Service
│   │
│   └── Admin Module
│       ├── Question Bank Manager (CRUD) -------> Connects to: Content Pipeline Service
│       └── User Manager (Access Control) ------> Connects to: User Service
│
│
└── BACKEND (Render / FastAPI + Python)
    │   # Responsible for business logic, validation, and database queries
    │
    ├── Auth Service (Token Verification, Role validation)
    ├── User Service (Profile management, Permissions)
    ├── Exam Delivery Service (Querying DB, Randomization, Pagination)
    ├── Grading Service (Answer checking, Score calculation, Analytics generation)
    ├── Content Pipeline Service (Handling CSV/OCR uploads, Data tagging)
    │
    └── database/
        │   # Firebase config co-located with the backend that consumes it
        ├── schema.md (Firestore collection definitions)
        └── firestore.rules (Security rules for Firestore)
