from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped

from app.database import Base


class Apartments(Base):
    __tablename__ = "apartments"

    title: Mapped[str]
    location: Mapped[str]
    price: Mapped[float]
    price_meters: Mapped[float]
    new: Mapped[bool]
    year: Mapped[int | None]
    room: Mapped[int]
    area: Mapped[float]
    floor: Mapped[int]
    type: Mapped[str]
    parking: Mapped[bool | None]
    repair: Mapped[str]
    balcony: Mapped[bool]
    district: Mapped[str]
