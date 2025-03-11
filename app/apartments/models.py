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
    year: Mapped[int]
    room: Mapped[int]
    area: Mapped[float]
    floor: Mapped[int]
    type: Mapped[int]
    parking: Mapped[bool]
    repair: Mapped[int]
    balcony: Mapped[bool]
    elevator: Mapped[bool]
    district: Mapped[str]
