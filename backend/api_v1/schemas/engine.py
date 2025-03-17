from typing import TYPE_CHECKING

from pydantic import BaseModel

if TYPE_CHECKING:
    from api_v1.schemas.car import CarBase


class EngineBase(BaseModel):
    engine_name: str
    base_price: int


class EngineCar(EngineBase):
    id: int
    photo_url: str


class EngineRead(EngineCar):
    cars: list["CarBase"] = []
    # если указать другую модель car, то будет ошибка, но якобы должны подгружаться помимо машин,
    # где используется двигатель еще и комплектующие машин, что по идеи тут не нужно

    class Config:
        from_attributes = True
