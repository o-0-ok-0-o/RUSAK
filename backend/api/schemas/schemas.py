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
    id: int
    car_name: str
    base_price: float


class EngineSchema(BaseModel):
    id: int
    engine_name: str
    base_price: float


class SaloneMembersSchema(BaseModel):
    id: int
    salone_name: str
    base_price: float


class SaloneOptionSchema(BaseModel):
    id: int
    salone_option_name: str
    base_price: float


class OptionShassiSchema(BaseModel):
    id: int
    shassi_name: str
    base_price: float


class OptionServiceSchema(BaseModel):
    id: int
    service_name: str
    base_price: float


class OptionZipSchema(BaseModel):
    id: int
    zip_name: str
    base_price: float
