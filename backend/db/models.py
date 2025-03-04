from enum import Enum
from utils.datetime import get_current_moscow_time
from datetime import datetime
from sqlalchemy import DateTime
from sqlalchemy.orm import Mapped, mapped_column
from .database import Base


class Order(Base):
    __tablename__ = "order"

    customer: Mapped[str]
    phone: Mapped[str]
    email: Mapped[str]


class Car(Base):
    __tablename__ = "cars"

    car_name: Mapped[str] = mapped_column(unique=True, index=True)
    base_price: Mapped[int]


class Engine(Base):
    __tablename__ = "engine"

    engine_name: Mapped[str] = mapped_column(unique=True, index=True)
    base_price: Mapped[int]


class SaloneMembers(Base):
    __tablename__ = "salone_members"

    salone_name: Mapped[str] = mapped_column(unique=True, index=True)
    base_price: Mapped[int]


class SaloneOption(Base):
    __tablename__ = "salone_option"

    salone_option_name: Mapped[str] = mapped_column(unique=True, index=True)
    base_price: Mapped[int]


class OptionShassi(Base):
    __tablename__ = "option_shassi"

    shassi_name: Mapped[str] = mapped_column(unique=True, index=True)
    base_price: Mapped[int]


class OptionService(Base):
    __tablename__ = "option_service"

    service_name: Mapped[str] = mapped_column(unique=True, index=True)
    base_price: Mapped[int]


class OptionZip(Base):
    __tablename__ = "option_zip"

    zip_name: Mapped[str] = mapped_column(unique=True, index=True)
    base_price: Mapped[int]
