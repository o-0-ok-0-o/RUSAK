from fastapi import Depends, Query, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from typing import Annotated
from api_v1.schemas.tire import TireBase
from db.database import get_async_session
from db.models import Tire


async def create_tire(
    tire: Annotated[TireBase, Depends()],
    session: AsyncSession = Depends(get_async_session),
):
    tire_dict: dict = tire.model_dump()
    tire_model = Tire(**tire_dict)
    session.add(tire_model)
    await session.commit()
    return tire


async def get_all_tires(
    session: AsyncSession,  # = Depends(get_async_session),
    offset: int = 0,
    limit: int = 100,
):
    tire = await session.execute(
        select(Tire).options(selectinload(Tire.cars)).offset(offset).limit(limit),
    )
    return tire.scalars().all()


async def get_tire(
    tire_id: int,
    session: AsyncSession = Depends(get_async_session),
):
    tire = await session.get(Tire, tire_id)

    if not tire:
        raise HTTPException(status_code=404, detail="Шина не найден")
    return tire


async def get_tire_price(
    tire_id: int,
    session: AsyncSession = Depends(get_async_session),
):
    result = await session.execute(select(Tire.base_price).where(Tire.id == tire_id))

    tire_price = result.scalar()

    if not tire_price:
        raise HTTPException(status_code=404, detail="Шинане найден")
    return tire_price


async def delete_tire(
    tire_id: int,
    session: AsyncSession = Depends(get_async_session),
):
    tire = await session.get(Tire, tire_id)

    if tire is None:
        raise HTTPException(status_code=404, detail="Шина не найдено")
    await session.delete(tire)
    await session.commit()
    return {"success": True}
