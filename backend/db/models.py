from typing import TYPE_CHECKING
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .association_table import (
    ZipCarAssociation,
    ServiceCarAssociation,
    ShassiCarAssociation,
    SaloneoptionCarAssociation,
)
from .database import Base


class Order(Base):
    __tablename__ = "order"

    customer: Mapped[str]
    phone: Mapped[str]
    email: Mapped[str]


class Car(Base):
    __tablename__ = "car"

    car_name: Mapped[str] = mapped_column(unique=True, index=True)
    base_price: Mapped[int]

    engine_id: Mapped[int] = mapped_column(
        ForeignKey("engine.id"),
    )
    engine: Mapped["Engine"] = relationship(back_populates="cars")

    salone_member_id: Mapped[int] = mapped_column(
        ForeignKey("salone_member.id"),
    )
    salone_member: Mapped["SaloneMember"] = relationship(back_populates="cars")

    tire_id: Mapped[int] = mapped_column(ForeignKey("tire.id"))
    tire: Mapped["Tire"] = relationship(back_populates="cars")

    wheelbase_id: Mapped[int] = mapped_column(ForeignKey("wheelbase.id"))
    wheelbase: Mapped["Wheelbase"] = relationship(back_populates="cars")

    salone_option: Mapped[list["SaloneOption"]] = relationship(
        secondary="saloneoption_car_association",
        back_populates="car",
    )
    zip: Mapped[list["Zip"]] = relationship(
        secondary="zip_car_association",
        back_populates="car",
    )
    shassi: Mapped[list["Shassi"]] = relationship(
        secondary="shassi_car_association",
        back_populates="car",
    )
    service: Mapped[list["Service"]] = relationship(
        secondary="service_car_association",
        back_populates="car",
    )


class Engine(Base):
    __tablename__ = "engine"

    engine_name: Mapped[str] = mapped_column(unique=True, index=True)
    base_price: Mapped[int]

    cars: Mapped[list["Car"]] = relationship(back_populates="engine")


class SaloneMember(Base):
    __tablename__ = "salone_member"

    salone_name: Mapped[str] = mapped_column(unique=True, index=True)
    base_price: Mapped[int]

    cars: Mapped[list["Car"]] = relationship(back_populates="salone_member")


class SaloneOption(Base):
    __tablename__ = "salone_option"

    salone_option_name: Mapped[str] = mapped_column(unique=True, index=True)
    base_price: Mapped[int]

    car: Mapped[list["Car"]] = relationship(
        secondary="saloneoption_car_association",
        back_populates="salone_option",
    )


class Shassi(Base):
    __tablename__ = "shassi"

    shassi_name: Mapped[str] = mapped_column(unique=True, index=True)
    base_price: Mapped[int]

    car: Mapped[list["Car"]] = relationship(
        secondary="shassi_car_association",
        back_populates="shassi",
    )


class Service(Base):
    __tablename__ = "service"

    service_name: Mapped[str] = mapped_column(unique=True, index=True)
    base_price: Mapped[int]

    car: Mapped[list["Car"]] = relationship(
        secondary="service_car_association",
        back_populates="service",
    )


class Zip(Base):
    __tablename__ = "zip"

    zip_name: Mapped[str] = mapped_column(unique=True, index=True)
    base_price: Mapped[int]

    car: Mapped[list["Car"]] = relationship(
        secondary="zip_car_association",
        back_populates="zip",
    )


class Tire(Base):
    __tablename__ = "tire"

    tire_name: Mapped[str] = mapped_column(unique=True, index=True)
    base_price: Mapped[int]

    cars: Mapped[list["Car"]] = relationship(back_populates="tire")


class Wheelbase(Base):
    __tablename__ = "wheelbase"

    wheelbase_name: Mapped[str] = mapped_column(unique=True, index=True)
    base_price: Mapped[int]

    cars: Mapped[list["Car"]] = relationship(back_populates="wheelbase")
