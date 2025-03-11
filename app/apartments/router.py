from http import HTTPStatus

from fastapi import APIRouter

from app.apartments.schemas import SApartments, SUploadDeleteResponse
from app.apartments.repository import ApartmentRepository

router = APIRouter(
    prefix="/apartments",
    tags=["apartments"],
)


@router.post('/upload_apart',
             summary='Добавить квартиру',
             description='<h1>Данный метод должен вызываться внутри парсера<h1>',
             response_model=SUploadDeleteResponse)
async def upload_apart(apart: SApartments):
    try:
        apartments = await ApartmentRepository.add_apartment(
            apart.title, apart.location, apart.price, apart.price_meters, apart.new, apart.year, apart.room, apart.area,
            apart.floor, apart.type, apart.parking, apart.repair, apart.balcony, apart.elevator, apart.district
        )
        return {
            "status_code": HTTPStatus.CREATED,
            "id": apartments.id,
            "message": f"Квартира {apartments.title} добавлена в базу"
        }
    except Exception as e:
        return {
            "status_code": HTTPStatus.INTERNAL_SERVER_ERROR,
            "id": -1,
            "message": str(e)
        }

@router.get('/get_apart/{apart_id}',
            summary='Получить квартиру',
            description='<h1>Данный метод возвращает квартиру с указаным id<h1>',)
async def get_apart(apart_id: int):
    apartment = await ApartmentRepository.get_apartment(apart_id)
    if apartment:
        return apartment
    return {
        "message": 'Не найденно'
    }

@router.delete('/delete_apart/{apart_id}',
               summary='Удалить квартиру',
               description='<h1>Данный метод удаляет квартиру с указаным id<h1>')
async def delete_apart(apart_id: int):
    apartment = await ApartmentRepository.get_apartment(apart_id)
    if not apartment:
        return {
            "status_code": HTTPStatus.NOT_FOUND,
            "id": apart_id,
            "message": f'Квартиры с id {apart_id} не существует'
        }
    await ApartmentRepository.delete_apartment(apart_id)
    return {
        "status_code": HTTPStatus.ACCEPTED,
        "id": apart_id,
        "message": 'Квартира успешно удалена'
    }