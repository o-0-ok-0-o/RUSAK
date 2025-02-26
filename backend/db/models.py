from enum import Enum
from typing import  Optional
from sqlmodel import Field, SQLModel
from utils.datetime import get_current_moscow_time


class OrderStatus(str, Enum):
    pending = "pending"
    processing = "processing"
    done = "done"
    cancelled = "cancelled"


class Order(SQLModel, table=True):
    """
    id: Уникальный идентификатор заказа
    order_date: Дата оформления заказа
    customer: Фио, сделавшего заказ
    total_amount: Общая сумма заказа
    status: Статус заказа
    shipping_address: Адрес
    """

    id: Optional[int] = Field(default=None, primary_key=True)
    order_date: str = Field(index=True)  # YYYY-MM-DD
    customer: str
    total_amount: int
    status: OrderStatus = Field(default=OrderStatus.pending)
    shipping_address: str
