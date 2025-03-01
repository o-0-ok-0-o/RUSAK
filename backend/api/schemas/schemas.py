from datetime import datetime

from pydantic import BaseModel
from db.models import OrderStatus, Order


# Заказы
class OrderBaseSchema(BaseModel):
    customer: str
    shipping_address: str

    class Config:
        from_attributes = True


class OrderCreateSchema(OrderBaseSchema):
    total_amount: int


class OrderSchema(OrderBaseSchema):
    id: int
    order_status: OrderStatus
    order_date: datetime


# Новые схемы надо поправить
class CarSchema(BaseModel):
    model: str
    base_price: float


class EngineSchema(BaseModel):
    color_name: str
    base_price: float


class SaloneMembersSchema(BaseModel):
    trim_name: str
    base_price: float


class SaloneOptionSchema(BaseModel):
    option_name: str
    base_price: float


class OptionShassiSchema(BaseModel):
    option_name: str
    base_price: float

    class ColorBase(BaseModel):
        color_name: str

    base_price: float


class OptionServisSchema(BaseModel):
    trim_name: str
    base_price: float


class OptionZipSchema(BaseModel):
    option_name: str
    base_price: float
