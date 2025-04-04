from typing import Optional, TYPE_CHECKING

from pydantic import BaseModel

if TYPE_CHECKING:
    from api_v1.schemas.car import CarBase


class WheelbaseBase(BaseModel):
    wheelbase_name: str
    base_price: int


class WheelbaseCar(WheelbaseBase):
    id: int
    photo_url: str


class WheelbaseRead(WheelbaseCar):
    car: list["CarBase"] = []

    class Config:
        from_attributes = True
