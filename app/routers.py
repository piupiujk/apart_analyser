from fastapi import APIRouter, Request
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException

from app.users.router import router as user_router
from app.apartments.router import router as apartment_router

router = APIRouter(tags=["API"], prefix="/api")

router.include_router(apartment_router)
router.include_router(user_router)


@router.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html(request: Request):
    return get_swagger_ui_html(
        openapi_url=f"{request.scope.get('root_path', '')}/openapi.json",
        title="API Documentation"
    )

@router.get("/openapi.json", include_in_schema=False)
async def get_openapi(request: Request):
    return request.app.openapi()