from fastapi import APIRouter

from app.users.router import router as user_router
from app.apartments.router import router as apartment_router

router = APIRouter()

router.include_router(apartment_router)
router.include_router(user_router)
