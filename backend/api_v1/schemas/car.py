from typing import Optional
from pydantic import BaseModel

from api_v1.schemas.engine import EngineCar
from api_v1.schemas.salone_member import SaloneMemberCar
from api_v1.schemas.salone_option import SaloneOptionCar
from api_v1.schemas.service import ServiceCar
from api_v1.schemas.shassi import ShassiCar
from api_v1.schemas.tire import TireCar
from api_v1.schemas.zip import ZipCar


class CarBase(BaseModel):
    car_name: str
    base_price: int
    engine_id: int
    salone_member_id: int
    tire_id: int
    photo_url: Optional[str]


class CarRead(CarBase):
    id: int

    engine: Optional[EngineCar] = None
    salone_member: Optional[SaloneMemberCar] = None
    tire: Optional[TireCar] = None

    salone_option: list[SaloneOptionCar] = []
    shassi: list[ShassiCar] = []
    service: list[ServiceCar] = []
    zip: list[ZipCar] = []

    class Config:
        from_attributes = True


class CalculatorBase(BaseModel):
    engine: int
    salone_member: int
    tire: int
    wheelbase: int
    salone_options: list[int]
    services: list[int]
    shassis: list[int]
    zips: list[int]
    total_price: int
