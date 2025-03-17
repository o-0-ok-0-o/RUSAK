from typing import Optional, TYPE_CHECKING

from pydantic import BaseModel

if TYPE_CHECKING:
    from api_v1.schemas.car import CarBase


class ZipBase(BaseModel):
    zip_name: str
    base_price: int
    photo_url: str


class ZipCar(ZipBase):
    id: int


class ZipRead(ZipCar):
    car: list["CarBase"] = []

    class Config:
        from_attributes = True
