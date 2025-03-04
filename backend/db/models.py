from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .association_table import (
    SaloneoptionCarAssociation,
    OptionzipCarAssociation,
    OptionserviceCarAssociation,
    OptionshassiCarAssociation,
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
    salone_members: Mapped[int] = mapped_column(
        ForeignKey("salone_members.id"),
    )

    salone_options: Mapped[list["SaloneOption"]] = relationship(
        secondary="saloneoption_car_association",
        back_populates="cars",
    )
    option_zip: Mapped[list["OptionZip"]] = relationship(
        secondary="optionzip_car_association",
        back_populates="cars",
    )
    option_shassi: Mapped[list["OptionShassi"]] = relationship(
        secondary="optionshassi_car_association",
        back_populates="cars",
    )
    options_service: Mapped[list["OptionService"]] = relationship(
        secondary="optionservice_car_association",
        back_populates="cars",
    )


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

    cars: Mapped[list["Car"]] = relationship(
        secondary="saloneoption_car_association",
        back_populates="salone_options",
    )


class OptionShassi(Base):
    __tablename__ = "option_shassi"

    shassi_name: Mapped[str] = mapped_column(unique=True, index=True)
    base_price: Mapped[int]

    cars: Mapped[list["Car"]] = relationship(
        secondary="optionshassi_car_association",
        back_populates="option_shassi",
    )


class OptionService(Base):
    __tablename__ = "option_service"

    service_name: Mapped[str] = mapped_column(unique=True, index=True)
    base_price: Mapped[int]

    cars: Mapped[list["Car"]] = relationship(
        secondary="optionservice_car_association",
        back_populates="option_service",
    )


class OptionZip(Base):
    __tablename__ = "option_zip"

    zip_name: Mapped[str] = mapped_column(unique=True, index=True)
    base_price: Mapped[int]

    cars: Mapped[list["Car"]] = relationship(
        secondary="optionzip_car_association",
        back_populates="option_zip",
    )
