from fastapi import FastAPI
from .routes import router as user_router

from .database import Base, engine
from . import models

# ✅ Create tables if they don't exist
Base.metadata.create_all(bind=engine)


app = FastAPI(title="Users Service")

# Include user-related routes
app.include_router(user_router, prefix="/users", tags=["users"])

# Optional: Root endpoint for health check
default_message = {"message": "User microservice is running"}

@app.get("/")
def read_root():
    return default_message
