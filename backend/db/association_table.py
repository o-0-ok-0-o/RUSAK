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


class ZipCarAssociation(Base):  # Zip - Car
    __tablename__ = "zip_car_association"
    table_name = (
        UniqueConstraint(
            "zip_id",
            "car_id",
            name="idx_unique_zip_car",
        ),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    zip_id: Mapped[int] = mapped_column(ForeignKey("zip.id"))
    car_id: Mapped[int] = mapped_column(ForeignKey("car.id"))


class ServiceCarAssociation(Base):  # Service - Car
    __tablename__ = "service_car_association"
    table_name = (
        UniqueConstraint(
            "service_id",
            "car_id",
            name="idx_unique_service_car",
        ),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    service_id: Mapped[int] = mapped_column(ForeignKey("service.id"))
    car_id: Mapped[int] = mapped_column(ForeignKey("car.id"))


class ShassiCarAssociation(Base):  # Shassi - Car
    __tablename__ = "shassi_car_association"
    table_name = (
        UniqueConstraint(
            "shassi_id",
            "car_id",
            name="idx_unique_shassi_car",
        ),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    shassi_id: Mapped[int] = mapped_column(ForeignKey("shassi.id"))
    car_id: Mapped[int] = mapped_column(ForeignKey("car.id"))
