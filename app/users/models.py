from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Users(Base):
    __tablename__ = 'users'

    email: Mapped[str]
    password: Mapped[str | None]
    tg_id: Mapped[int | None]
    balance: Mapped[float] = mapped_column(default=0)
    role: Mapped[int] = mapped_column(default=1)
