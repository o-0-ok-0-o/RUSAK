from enum import Enum
from utils.datetime import get_current_moscow_time
from datetime import datetime
from sqlalchemy import DateTime
from sqlalchemy.orm import Mapped, mapped_column
from .database import Base


class OrderStatus(str, Enum):
    pending = "pending"
    processing = "processing"
    done = "done"
    cancelled = "cancelled"


class Order(Base):
    __tablename__ = "order"

    id: Mapped[int] = mapped_column(primary_key=True)
    order_date: Mapped[str] = mapped_column(default=get_current_moscow_time())
    customer: Mapped[str]
    total_amount: Mapped[int]
    status: Mapped[OrderStatus] = mapped_column(default=OrderStatus.pending)
    shipping_address: Mapped[str]
