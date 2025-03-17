from fastapi import Depends, Query, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from typing import Annotated
from api_v1.schemas.schemas import WheelbaseBase
from db.database import get_async_session
from db.models import Wheelbase


async def create_wheelbase(
    wheelbase: Annotated[WheelbaseBase, Depends()],
    session: AsyncSession = Depends(get_async_session),
):
    wheelbase_dict: dict = wheelbase.model_dump()
    wheelbase_model = Wheelbase(**wheelbase_dict)
    session.add(wheelbase_model)
    await session.commit()
    return wheelbase


async def get_all_wheelbases(
    session: AsyncSession,  # = Depends(get_async_session),
    offset: int = 0,
    limit: int = 100,
):
    wheelbases = await session.execute(
        select(Wheelbase)
        .options(selectinload(Wheelbase.cars))
        .offset(offset)
        .limit(limit),
    )
    return wheelbases.scalars().all()


async def get_wheelbase(
    wheelbase_id: int,
    session: AsyncSession,
):
    wheelbase = await session.get(Wheelbase, wheelbase_id)

    if not wheelbase:
        raise HTTPException(status_code=404, detail="Колесная база не найден")
    return wheelbase


async def get_wheelbase_price(
    wheelbase_id: int,
    session: AsyncSession = Depends(get_async_session),
):
    result = await session.execute(
        select(Wheelbase.base_price).where(Wheelbase.id == wheelbase_id)
    )

    wheelbase_price = result.scalar()

    if not wheelbase_price:
        raise HTTPException(status_code=404, detail="Колесная база не найден")
    return wheelbase_price


async def delete_wheelbase(
    wheelbase_id: int,
    session: AsyncSession = Depends(get_async_session),
):
    wheelbase = await session.get(Wheelbase, wheelbase_id)

    if wheelbase is None:
        raise HTTPException(status_code=404, detail="Колесная база не найден")
    await session.delete(wheelbase)
    await session.commit()
    return {"success_delete": True}
