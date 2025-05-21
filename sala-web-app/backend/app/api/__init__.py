from fastapi import APIRouter
from app.api.endpoints.upload import router as upload_router

# Create the main API router
api_router = APIRouter()

# Include the upload router
api_router.include_router(upload_router, prefix="/upload", tags=["Upload"])