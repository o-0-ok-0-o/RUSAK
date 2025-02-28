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
