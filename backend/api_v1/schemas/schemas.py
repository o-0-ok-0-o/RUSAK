import re

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


# Новые схемы надо поправить
# class CarSchema(BaseModel):
#     id: int
#     car_name: str
#     base_price: float
#
#
# class EngineSchema(BaseModel):
#     id: int
#     engine_name: str
#     base_price: float
#
#
# class SaloneMembersSchema(BaseModel):
#     id: int
#     salone_name: str
#     base_price: float
#
#
# class SaloneOptionSchema(BaseModel):
#     id: int
#     salone_option_name: str
#     base_price: float
#
#
# class OptionShassiSchema(BaseModel):
#     id: int
#     shassi_name: str
#     base_price: float
#
#
# class OptionServiceSchema(BaseModel):
#     id: int
#     service_name: str
#     base_price: float
#
#
# class OptionZipSchema(BaseModel):
#     id: int
#     zip_name: str
#     base_price: float
