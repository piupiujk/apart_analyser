from pydantic import BaseModel


class SApartments(BaseModel):
    title: str
    location: str
    price: float
    price_meters: float
    new: bool
    year: int
    room: int
    area: float
    floor: int
    type: int
    parking: bool
    repair: int
    balcony: bool
    elevator: bool
    district: str


class SUploadResponse(BaseModel):
    status_code: int
    id: int
    message: str
