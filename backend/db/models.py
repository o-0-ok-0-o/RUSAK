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


class Car(Base):
    __tablename__ = "cars"

    id: Mapped[int] = mapped_column(primary_key=True)
    car_name: Mapped[str] = mapped_column(unique=True, index=True)
    base_price: Mapped[int]


class Engine(Base):
    __tablename__ = "engine"

    id: Mapped[int] = mapped_column(primary_key=True)
    engine_name: Mapped[str] = mapped_column(unique=True, index=True)
    base_price: Mapped[int]


class SaloneMembers(Base):
    __tablename__ = "salone_members"

    id: Mapped[int] = mapped_column(primary_key=True)
    salone_name: Mapped[str] = mapped_column(unique=True, index=True)
    base_price: Mapped[int]


class SaloneOption(Base):
    __tablename__ = "salone_option"

    id: Mapped[int] = mapped_column(primary_key=True)
    salone_option_name: Mapped[str] = mapped_column(unique=True, index=True)
    base_price: Mapped[int]


class OptionShassi(Base):
    __tablename__ = "option_shassi"

    id: Mapped[int] = mapped_column(primary_key=True)
    shassi_name: Mapped[str] = mapped_column(unique=True, index=True)
    base_price: Mapped[int]


class OptionService(Base):
    __tablename__ = "option_service"

    id: Mapped[int] = mapped_column(primary_key=True)
    service_name: Mapped[str] = mapped_column(unique=True, index=True)
    base_price: Mapped[int]


class OptionZip(Base):
    __tablename__ = "option_zip"

    id: Mapped[int] = mapped_column(primary_key=True)
    zip_name: Mapped[str] = mapped_column(unique=True, index=True)
    base_price: Mapped[int]
