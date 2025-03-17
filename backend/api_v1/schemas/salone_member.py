from typing import Optional, TYPE_CHECKING

from pydantic import BaseModel

if TYPE_CHECKING:
    from api_v1.schemas.car import CarBase


class SaloneMemberBase(BaseModel):
    salone_name: str
    base_price: int
    photo_url: Optional[str]


class SaloneMemberCar(SaloneMemberBase):
    id: int


class SaloneMemberRead(SaloneMemberCar):
    cars: list["CarBase"] = []
    # если указать другую модель car, то будет ошибка, но якобы должны подгружаться помимо машин,
    # где используется двигатель еще и комплектующие машин, что по идеи тут не нужно

    class Config:
        from_attributes = True
