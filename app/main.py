from fastapi import FastAPI
from app.api.v1 import endpoints

app = FastAPI(title="Khyal.ai Backend", version="0.1.0")

# Include API v1 routes
app.include_router(endpoints.router, prefix="/api/v1")

@app.get("/")
async def root():
    return {"message": "Welcome to Khyal.ai API 🚀"}
