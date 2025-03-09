from fastapi import Depends, Query, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from typing import Annotated
from api_v1.schemas.schemas import EngineBase
from db.database import get_async_session
from db.models import Engine


async def create_engine(
    engine: Annotated[EngineBase, Depends()],
    session: AsyncSession = Depends(get_async_session),
):
    engine_dict: dict = engine.model_dump()
    engine_model = Engine(**engine_dict)
    session.add(engine_model)
    await session.commit()
    return engine


async def get_all_engines(
    session: AsyncSession,  # = Depends(get_async_session),
    offset: int = 0,
    limit: int = 100,
):
    engines = await session.execute(
        select(Engine).options(selectinload(Engine.cars)).offset(offset).limit(limit),
    )
    return engines.scalars().all()


async def get_engine(
    engine_id: int,
    session: AsyncSession,
):
    engine = await session.get(Engine, engine_id)

    if not engine:
        raise HTTPException(status_code=404, detail="Двигатель не найден")
    return engine


async def get_engine_price(
    engine_id: int,
    session: AsyncSession = Depends(get_async_session),
):
    result = await session.execute(
        select(Engine.base_price).where(Engine.id == engine_id)
    )

    engine_price = result.scalar()

    if not engine_price:
        raise HTTPException(status_code=404, detail="Двигатель не найден")
    return engine_price


async def delete_engine(
    engine_id: int,
    session: AsyncSession = Depends(get_async_session),
):
    engine = await session.get(Engine, engine_id)

    if engine is None:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    await session.delete(engine)
    await session.commit()
    return {"success_delete": True}
