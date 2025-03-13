from http import HTTPStatus
from typing import Optional, List

from fastapi import APIRouter, Query

from app.apartments.schemas import SApartments, SUploadDeleteResponse
from app.apartments.repository import ApartmentRepository

router = APIRouter(
    prefix="/apartments",
    tags=["Квартиры"],
)


@router.post('/upload_apart',
             summary='Добавить квартиру',
             description='<h1>Данный метод должен вызываться внутри парсера<h1>',
             response_model=SUploadDeleteResponse)
async def upload_apart(apart: SApartments):
    try:
        apartments = await ApartmentRepository.add_apartment(
            apart.title, apart.location, apart.price, apart.price_meters, apart.new, apart.year, apart.room, apart.area,
            apart.floor, apart.type, apart.parking, apart.repair, apart.balcony, apart.district)
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
            summary='Получить квартиру по id',
            description='<h1>Данный метод возвращает квартиру с указаным id<h1>', )
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


@router.get('/get_apart',
            summary='Получить квартиры по фильтрам',
            description='<h1>Данный метод возвращает квартиры, которые подходят по фильтрам<h1>',
            response_model=list[SApartments])
async def get_apart(
        price_from: Optional[float] = Query(0, ge=0, le=50000000),
        price_to: Optional[float] = Query(50000000, ge=0, le=50000000),
        price_meters_from: Optional[float] = Query(0, ge=0, le=1000000),
        price_meters_to: Optional[float] = Query(1000000, ge=0, le=1000000),
        new: Optional[bool] = None,
        year_from: Optional[int] = Query(None, ge=1700, le=2025),
        year_to: Optional[int] = Query(None, ge=1700, le=2025),
        room_from: Optional[int] = Query(0, ge=0, le=20),
        room_to: Optional[int] = Query(20, ge=0, le=20),
        area_from: Optional[float] = Query(0, ge=0, le=2000),
        area_to: Optional[float] = Query(2000, ge=0, le=2000),
        floor_from: Optional[int] = Query(0, ge=0, le=50),
        floor_to: Optional[int] = Query(50, ge=0, le=50),
        type: Optional[str] = None,
        parking: Optional[bool] = None,
        repair: Optional[str] = None,
        balcony: Optional[bool] = None,
):
    apartment = await ApartmentRepository.get_apartment_with_filter(price_from, price_to, price_meters_from,
                                                                    price_meters_to, new, year_from, year_to,
                                                                    room_from, room_to, area_from, area_to,
                                                                    floor_from, floor_to, type, parking, repair,
                                                                    balcony)

    return apartment
