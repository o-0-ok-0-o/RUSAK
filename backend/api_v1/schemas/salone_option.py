from typing import Optional, TYPE_CHECKING

from pydantic import BaseModel

if TYPE_CHECKING:
    from api_v1.schemas.car import CarBase


class SaloneOptionBase(BaseModel):
    salone_option_name: str
    base_price: int
    photo_url: Optional[str]


class SaloneOptionCar(SaloneOptionBase):
    id: int


class SaloneOptionRead(SaloneOptionCar):
    car: list["CarBase"] = []

    class Config:
        from_attributes = True
