from fastapi import APIRouter

from app.apartments.schemas import SApartments

router = APIRouter(
    prefix="/apartments",
    tags=["apartments"],
)


@router.post('/upload_apart',
             summary='Добавить квартиру',
             description='<h1>Данный метод должен вызываться внутри парсера<h1>', )
async def upload_apart(apart: SApartments):
    pass
