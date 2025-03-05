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


# Двигатель
class EngineBase(BaseModel):
    engine_name: str
    base_price: int


class EngineRead(EngineBase):
    id: int
    cars: list["CarRead"] = []

    class Config:
        from_attributes = True


# Салон кол-во
class SaloneMemberBase(BaseModel):
    salone_name: str
    base_price: int


class SaloneMemberRead(SaloneMemberBase):
    id: int
    cars: list["CarRead"] = []

    class Config:
        from_attributes = True


class SaloneOptionBase(BaseModel):
    salone_option_name: str
    base_price: int


# Салон опции
class SaloneOptionRead(SaloneOptionBase):
    id: int

    class Config:
        from_attributes = True


class ShassiBase(BaseModel):
    shassi_name: str
    base_price: int


# Шасси
class ShassiRead(ShassiBase):
    id: int

    class Config:
        from_attributes = True


class ServiceBase(BaseModel):
    service_name: str
    base_price: int


# Сервис
class ServiceRead(ServiceBase):
    id: int

    class Config:
        from_attributes = True


class ZipBase(BaseModel):
    zip_name: str
    base_price: int


# Зип
class ZipRead(ZipBase):
    id: int

    class Config:
        from_attributes = True


# Машина
class CarBase(BaseModel):
    car_name: str
    base_price: int
    engine_id: int
    salone_member_id: int


class CarRead(CarBase):
    id: int

    engine: Optional[EngineRead] = None
    salone_member: Optional[SaloneMemberRead] = None

    salone_option: list[SaloneOptionRead] = []
    shassi: list[ShassiRead] = []
    service: list[ServiceRead] = []
    zip: list[ZipRead] = []

    class Config:
        from_attributes = True
