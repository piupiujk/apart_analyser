from http import HTTPStatus

from fastapi import APIRouter

from app.apartments.schemas import SApartments, SUploadResponse
from app.apartments.repository import ApartmentRepository

router = APIRouter(
    prefix="/apartments",
    tags=["apartments"],
)


@router.post('/upload_apart',
             summary='Добавить квартиру',
             description='<h1>Данный метод должен вызываться внутри парсера<h1>',
             response_model=SUploadResponse)
async def upload_apart(apart: SApartments):
    apartments = await ApartmentRepository.add_apartment(
        apart.title, apart.location, apart.price, apart.price_meters, apart.new, apart.year, apart.room, apart.area,
        apart.floor, apart.type, apart.parking, apart.repair, apart.balcony, apart.elevator, apart.district
    )
    return {"status_code": HTTPStatus.CREATED,
            "id": apartments.id,
            "message": f"Квартира {apartments.title} добавлена в базу"}

@router.get('/get_apart',
            summary='Получить квартиру',
            description='<h1>Данный метод возвращает квартиру с указаным id<h1>',)
async def get_apart(apart_id: int):
    apartment = await ApartmentRepository.get_apartment(apart_id)
    return apartment