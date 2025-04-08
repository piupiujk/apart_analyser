from pydantic import EmailStr
from sqlalchemy import delete, select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import async_session

from app.users.models import Users

class UserRepository:
    @classmethod
    async def find_one_or_none(cls, email: EmailStr):
        async with async_session() as session:
            query = select(Users).filter_by(email=email)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    @classmethod
    async def find_by_tg_id(cls, tg_id: int):
        async with async_session() as session:
            query = select(Users).filter_by(tg_id=tg_id)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    @classmethod
    async def find_by_email(cls, email: str):
        async with async_session() as session:
            query = select(Users).filter_by(email=email)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    @classmethod
    async def add_user(cls, email: EmailStr, password: str):
        async with async_session() as session:
            query = insert(Users).values(email=email, password=password)
            await session.execute(query)
            await session.commit()