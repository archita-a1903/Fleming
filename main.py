from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import Base, engine
from .routers import triage, doctors, admin

app = FastAPI(title="Fleming API (Local SQLite MVP)")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

app.include_router(triage.router)
app.include_router(doctors.router)
app.include_router(admin.router)

@app.get("/health")
def health():
    return {"ok": True}
