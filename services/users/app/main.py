print("🚀 CI Test Triggered!!")
from fastapi import FastAPI
from contextlib import asynccontextmanager
from .routes import router as user_router
from .database import Base, engine
from . import models

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Create DB tables at app startup
    Base.metadata.create_all(bind=engine)
    yield

app = FastAPI(title="Users Service", lifespan=lifespan)

# Include user-related routes
app.include_router(user_router, prefix="/users", tags=["users"])

# Optional: Root endpoint for health check
default_message = {"message": "User microservice is running"}

@app.get("/")
def read_root():
    return default_message

@app.get("/health")
def health_check():
    return {"status": "ok"}
