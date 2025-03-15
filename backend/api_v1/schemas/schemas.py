import re
from typing import Optional

from pydantic import BaseModel, EmailStr, Field, field_validator


# Заказы
class OrderBaseSchema(BaseModel):
    customer: str
    phone: str = Field(
        default=...,
        description="Номер телефона в международном формате, начинающийся с '+'",
    )
    email: EmailStr = Field(default=..., description="Электронная почта студента")

    @field_validator("phone", check_fields=False)
    @classmethod
    def validate_phone_number(cls, phone_number: str) -> str:
        if not re.match(r"^\+7\d{10}$", phone_number):
            raise ValueError(
                'Номер телефона должен начинаться с "+7" и содержать 11 цифр'
            )
        return phone_number


class OrderCreateSchema(OrderBaseSchema):
    pass


class OrderSchema(OrderBaseSchema):
    id: int

    class Config:
        from_attributes = True


from fastapi import File


# Двигатель
class EngineBase(BaseModel):
    engine_name: str
    base_price: int


class EngineCar(EngineBase):
    id: int


class EngineRead(EngineCar):
    cars: list["CarBase"] = []
    # если указать другую модель car, то будет ошибка, но якобы должны подгружаться помимо машин,
    # где используется двигатель еще и комплектующие машин, что по идеи тут не нужно

    class Config:
        from_attributes = True


# Салон кол-во
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


# Салон опции
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


# Шасси
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


# Сервис
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


# Зип
class ZipBase(BaseModel):
    zip_name: str
    base_price: int
    photo_url: Optional[str]


class ZipCar(ZipBase):
    id: int


class ZipRead(ZipCar):
    car: list["CarBase"] = []

    class Config:
        from_attributes = True


# Шина
class TireBase(BaseModel):
    tire_name: str
    base_price: int
    photo_url: Optional[str]


class TireCar(TireBase):
    id: int


class TireRead(TireCar):
    car: list["CarBase"] = []

    class Config:
        from_attributes = True


# Колесная база
class WheelbaseBase(BaseModel):
    wheelbase_name: str
    base_price: int
    photo_url: Optional[str]


class WheelbaseCar(WheelbaseBase):
    id: int


class WheelbaseRead(WheelbaseCar):
    car: list["CarBase"] = []

    class Config:
        from_attributes = True


# Машина
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
