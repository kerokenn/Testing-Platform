# Testing-PlatformV1
Wu and Co.


Testing-Platform/
│
├── FRONTEND (Vercel / Next.js) 
│   │   # Responsible for UI, routing, and user experience
│   │
│   ├── Public Module
│   │   ├── Landing Page -----------------------> (Reads static/cached data)
│   │   └── Auth Pages (Login/Register) --------> Connects to: Auth Service
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
├── BACKEND (Render / Node.js or Python API)
│   │   # Responsible for business logic, validation, and database queries
│   │
│   ├── Auth Service (JWT Generation, Login validation)
│   ├── User Service (Profile management, Role verification)
│   ├── Exam Delivery Service (Querying DB, Randomization, Pagination)
│   ├── Grading Service (Answer checking, Score calculation, Analytics generation)
│   └── Content Pipeline Service (Handling CSV/OCR uploads, Data tagging)
│
│
└── DATABASE (PostgreSQL)
        # The single source of truth queried ONLY by the Render Backend
        ├── Users Table
        ├── Exams/Categories Table
        ├── Questions & Choices Table
        └── Historical Results Table
