# Testing-PlatformV1
Wu and Co.


# Mock Testing Platform

A scalable, modular web application designed for high-concurrency exam delivery, automated grading, and real-time data synchronization.



## 🏗 System Architecture

The project follows a decoupled **Client-Server architecture**, utilizing **Firebase** for real-time data persistence and simplified backend integration.

### 1. Frontend (Next.js)
*Deployed on Vercel*
* **Public Module:** Manages the landing experience and initial user onboarding.
* **Examinee Module:** Optimized for performance during active testing, utilizing local state for timers and Firebase for progress persistence.
* **Admin Module:** A secure dashboard for CRUD operations on question banks and managing user access levels.

### 2. Backend (Node.js/Python API)
*Deployed on Render*
* **Auth Service:** Integration with Firebase Auth for secure JWT-based sessions.
* **Exam Delivery Service:** Handles randomization logic and pagination to ensure integrity.
* **Grading & Analytics:** Processes raw exam data into digestible performance metrics.
* **Content Pipeline:** Bulk-upload engine for processing CSV and OCR data into the Firebase schema.

### 3. Database (Firebase)
*The Real-time Source of Truth*
* **Firestore/Realtime DB:** Flexible, NoSQL document-based storage queried by the Render Backend for business logic and validation.

---

## 📂 Project Structure

```text
mock-testing-platform/
│
├── FRONTEND (Next.js) 
│   ├── Public Module        # Landing Page, Auth (Login/Register)
│   ├── Examinee Module      # Dashboard, Exam Catalog, Active Exam UI, Results
│   └── Admin Module         # Question Bank Manager, User Manager
│
├── BACKEND (API)
│   ├── Auth Service         # Firebase Auth Validation & JWT
│   ├── User Service         # Profile management & Role Verification
│   ├── Exam Delivery        # Randomization & Pagination Logic
│   ├── Grading Service      # Score calculation & Analytics
│   └── Content Pipeline     # CSV/OCR uploads & Data tagging
│
└── DATABASE (Firebase)
    ├── Users Collection      # Profiles, Roles, and Metadata
    ├── Exams Collection      # Categories and Test Metadata
    ├── Questions Collection  # Bank of questions & choice mappings
    └── Results Collection    # Historical performance data
