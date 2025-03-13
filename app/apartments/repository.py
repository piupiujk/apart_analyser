from sqlalchemy import delete, select

from app.database import async_session
from app.apartments.models import Apartments


class ApartmentRepository:
    @classmethod
    async def add_apartment(cls, title, location, price, price_meters, new, year, room, area, floor, type, parking,
                            repair, balcony, district):
        async with async_session() as session:
            new_apartment = Apartments(title=title, location=location, price=price, price_meters=price_meters,
                                       new=new, year=year, room=room, area=area, floor=floor, type=type,
                                       parking=parking,
                                       repair=repair, balcony=balcony, district=district)
            session.add(new_apartment)
            await session.commit()
            await session.refresh(new_apartment)
            return new_apartment

    @classmethod
    async def delete_apartment(cls, apartment_id):
        async with async_session() as session:
            query = delete(Apartments).where(Apartments.id == apartment_id)
            await session.execute(query)
            await session.commit()

    @classmethod
    async def get_apartment(cls, apart_id: int):
        async with async_session() as session:
            query = select(Apartments).where(Apartments.id == apart_id)
            result = await session.execute(query)
            apartment = result.scalar()
            return apartment

    @classmethod
    async def get_apartment_with_filter(cls, price_from: float,
                                        price_to: float,
                                        price_meters_from: float,
                                        price_meters_to: float,
                                        new: bool | None,
                                        year_from: int,
                                        year_to: int,
                                        room_from: int,
                                        room_to: int,
                                        area_from: float,
                                        area_to: float,
                                        floor_from: int,
                                        floor_to: int,
                                        type: str | None,
                                        parking: bool | None,
                                        repair: str | None,
                                        balcony: bool | None
                                        ):
        async with async_session() as session:
            query = select(Apartments)
            query = query.where(Apartments.price.between(price_from, price_to))
            query = query.where(Apartments.price_meters.between(price_meters_from, price_meters_to))
            query = query.where(Apartments.room.between(room_from, room_to))
            query = query.where(Apartments.area.between(area_from, area_to))
            query = query.where(Apartments.floor.between(floor_from, floor_to))

            if year_from is not None:
                query = query.where(Apartments.year >= year_from)

            if year_to is not None:
                query = query.where(Apartments.year <= year_to)

            if new is not None:
                query = query.where(Apartments.new == new)

            if type is not None:
                query = query.where(Apartments.type == type)

            if parking is not None:
                query = query.where(Apartments.parking == parking)

            if repair is not None:
                query = query.where(Apartments.repair == repair)

            if balcony is not None:
                query = query.where(Apartments.balcony == balcony)

            result = await session.execute(query)
            return result.scalars().all()
