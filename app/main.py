from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from app.routers import router as api_router

app = FastAPI(
    title='Анализ квартир',
    docs_url=None,
    redoc_url=None
)

app.include_router(api_router)

@app.get('/', summary='Главная страница', tags=['Главная страница'])
def home_page():
    return {'message': 'Главная страница'}

@app.exception_handler(404)
async def api_not_found_handler(request: Request, exc: HTTPException):
    if request.url.path.startswith("/api"):
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"success": False, "msg": "Неизвестный метод"}
        )
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"detail": "404 page"}
    )