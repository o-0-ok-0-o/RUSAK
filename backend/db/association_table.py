from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import mapped_column, Mapped

from db.database import Base


class SaloneoptionCarAssociation(Base):  # SaloneOption - Car
    __tablename__ = "saloneoption_car_association"
    table_name = (
        UniqueConstraint(
            "saloneoption_id",
            "car_id",
            name="idx_unique_saloneoption_car",
        ),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    salone_option_id: Mapped[int] = mapped_column(ForeignKey("salone_option.id"))
    car_id: Mapped[int] = mapped_column(ForeignKey("car.id"))


class OptionzipCarAssociation(Base):  # Zip - Car
    __tablename__ = "optionzip_car_association"
    table_name = (
        UniqueConstraint(
            "optionzip_id",
            "car_id",
            name="idx_unique_optionzip_car",
        ),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    optionzip_id: Mapped[int] = mapped_column(ForeignKey("option_zip.id"))
    car_id: Mapped[int] = mapped_column(ForeignKey("car.id"))


class OptionserviceCarAssociation(Base):  # Service - Car
    __tablename__ = "optionservice_car_association"
    table_name = (
        UniqueConstraint(
            "optionservice_id",
            "car_id",
            name="idx_unique_optionservice_car",
        ),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    optionservice_id: Mapped[int] = mapped_column(ForeignKey("option_service.id"))
    car_id: Mapped[int] = mapped_column(ForeignKey("car.id"))


class OptionshassiCarAssociation(Base):  # Shassi - Car
    __tablename__ = "option_shassi_car_association"
    table_name = (
        UniqueConstraint(
            "option_shassi_id",
            "car_id",
            name="idx_unique_option_shassi_car",
        ),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    option_shassi_id: Mapped[int] = mapped_column(ForeignKey("option_shassi.id"))
    car_id: Mapped[int] = mapped_column(ForeignKey("car.id"))
