from typing import Optional, TYPE_CHECKING

from pydantic import BaseModel

if TYPE_CHECKING:
    from api_v1.schemas.car import CarBase


class ShassiBase(BaseModel):
    shassi_name: str
    base_price: int
    photo_url: Optional[str]


class ShassiCar(ShassiBase):
    id: int


class ShassiRead(ShassiCar):
    car: list["CarBase"] = []

    class Config:
        from_attributes = True
