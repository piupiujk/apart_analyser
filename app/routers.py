from fastapi import APIRouter

from app.apartments.router import router as apartment_router

router = APIRouter()

router.include_router(apartment_router)
