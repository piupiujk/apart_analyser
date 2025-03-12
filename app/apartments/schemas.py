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
    type: str
    parking: bool | None
    repair: str
    balcony: bool
    district: str


class SUploadDeleteResponse(BaseModel):
    status_code: int
    id: int
    message: str
