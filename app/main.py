from fastapi import FastAPI
from app.api.v1.routes import router
from app.core.config import settings

app = FastAPI(title=settings.PROJECT_NAME)

# 🏠 Root endpoint
@app.get("/")
async def home():
    return {"message": "Hello, World!"}

# 📦 API v1 routes
app.include_router(router, prefix="/api/v1")
