from fastapi import FastAPI

from app.database.connection import Base, engine
from app.models import user
from app.api.users import router as users_router

app = FastAPI(
    title="Researcher.ai",
    description="Intelligent Knowledge and Research Platform",
    version="1.0.0",
)

# Create database tables
Base.metadata.create_all(bind=engine)
app.include_router(users_router)


@app.get("/")
def home():
    return {"message": "Welcome to Researcher.ai", "status": "Running"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}
