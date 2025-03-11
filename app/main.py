from fastapi import FastAPI
from app.routers import router as main_router

app = FastAPI(title='Анализ квартир')


@app.get('/', summary='Главная страница', tags=['Главная страница'])
def home_page():
    return {'message': 'Главная страница'}


app.include_router(main_router)
