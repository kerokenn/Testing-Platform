from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import auth, users, exams, grading, content

app = FastAPI(title="Testing Platform API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # TODO: restrict to your Vercel domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(exams.router)
app.include_router(grading.router)
app.include_router(content.router)


@app.get("/")
def health_check():
    return {"status": "ok"}
