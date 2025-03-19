from fastapi import HTTPException, UploadFile
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from typing import Annotated, Optional

from utils.photo import create_photo
from api_v1.schemas.car import CarBase
from db.models import Car


async def create_car(
    car: CarBase,
    engine: Optional[CarBase] = None
    salone_member: Optional[SaloneMemberCar] = None
    tire: Optional[Car] = None

    salone_option: list[SaloneOptionCar] = []
    shassi: list[ShassiCar] = []
    service: list[ServiceCar] = []
    zip: list[ZipCar] = []
    photo: UploadFile,
    session: AsyncSession,
):
    try:
        file_path = await create_photo(photo)
        car_dict: dict = car.model_dump()
        car_dict["photo_url"] = file_path
        car_model = Car(**car_dict)

        session.add(car_model)
        await session.commit()
        await session.refresh(car_model)
        return car_model
    except Exception as e:
        await session.rollback()
        raise e


async def get_all_cars(
    session: AsyncSession,
    offset: int = 0,
    limit: int = 100,
):
    cars = await session.execute(
        select(Car).options(selectinload(Car.cars)).offset(offset).limit(limit),
    )
    return cars.scalars().all()


async def get_car(
    car_id: int,
    session: AsyncSession,
):
    car = await session.get(Car, car_id)

    if not car:
        raise HTTPException(status_code=404, detail="Двигатель не найден")
    return car


async def get_car_price(
    car_id: int,
    session: AsyncSession,
):
    result = await session.execute(select(Car.base_price).where(Car.id == car_id))

    car_price = result.scalar()

    if not car_price:
        raise HTTPException(status_code=404, detail="Двигатель не найден")
    return car_price


async def delete_car(
    car_id: int,
    session: AsyncSession,
):
    car = await session.get(Car, car_id)

    if car is None:
        raise HTTPException(status_code=404, detail="Двигатель не найден")
    await session.delete(car)
    await session.commit()
    return {"success_delete": True}
