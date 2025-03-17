from typing import Optional, TYPE_CHECKING

from pydantic import BaseModel

if TYPE_CHECKING:
    from api_v1.schemas.car import CarBase


class ServiceBase(BaseModel):
    service_name: str
    base_price: int
    photo_url: Optional[str]


class ServiceCar(ServiceBase):
    id: int


class ServiceRead(ServiceCar):
    car: list["CarBase"] = []

    class Config:
        from_attributes = True
