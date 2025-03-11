from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped

from app.database import Base


class Users(Base):
    __tablename__ = 'users'

    login: Mapped[str]
    password: Mapped[str]
    tg_id: Mapped[int | None]
    balance: Mapped[float]
    role: Mapped[int]
