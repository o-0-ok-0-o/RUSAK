from typing import Optional, TYPE_CHECKING

from pydantic import BaseModel

if TYPE_CHECKING:
    from api_v1.schemas.car import CarBase


class TireBase(BaseModel):
    tire_name: str
    base_price: int


class TireCar(TireBase):
    id: int
    photo_url: str


class TireRead(TireCar):
    car: list["CarBase"] = []

    class Config:
        from_attributes = True
