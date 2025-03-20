from typing import Optional
from pydantic import BaseModel

from api_v1.schemas.engine import EngineCar
from api_v1.schemas.salone_member import SaloneMemberCar
from api_v1.schemas.salone_option import SaloneOptionCar
from api_v1.schemas.service import ServiceCar
from api_v1.schemas.shassi import ShassiCar
from api_v1.schemas.tire import TireCar
from api_v1.schemas.wheelbase import WheelbaseCar
from api_v1.schemas.zip import ZipCar


class CarBase(BaseModel):
    car_name: str
    base_price: int
    engine_id: int
    salone_member_id: int
    tire_id: int
    wheelbase: int


class CarRead(BaseModel):
    id: int
    car_name: str
    base_price: int
    photo_url: str

    engine: EngineCar
    salone_member: SaloneMemberCar
    tire: TireCar
    wheelbase: WheelbaseCar

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
