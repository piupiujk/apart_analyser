from sqlalchemy import delete, select

from app.database import async_session
from app.apartments.models import Apartments


class ApartmentRepository:
    @classmethod
    async def add_apartment(cls, title, location, price, price_meters, new, year, room, area, floor, type, parking,
                            repair, balcony, elevator, district):
        async with async_session() as session:
            new_apartment = Apartments(title=title, location=location, price=price, price_meters=price_meters,
                                       new=new, year=year, room=room, area=area, floor=floor, type=type, parking=parking,
                                       repair=repair, balcony=balcony, elevator=elevator, district=district)
            session.add(new_apartment)
            await session.commit()
            await session.refresh(new_apartment)

    @classmethod
    async def get_apartment(cls, apart_id: int):
        async with async_session() as session:
            query = select(Apartments).where(Apartments.id == apart_id)
            result = await session.execute(query).scalar()
            return result
