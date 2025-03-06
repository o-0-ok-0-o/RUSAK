from fastapi import Depends, Query, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from typing import Annotated
from api_v1.schemas.schemas import SaloneMemberBase
from db.database import get_async_session
from db.models import Shassi


async def create_shassi(
    shassi1: Annotated[SaloneMemberBase, Depends()],
    session: AsyncSession = Depends(get_async_session),
):
    shassi_dict: dict = shassi1.model_dump()
    shassi_model = Shassi(**shassi_dict)
    session.add(shassi_model)
    await session.commit()
    return shassi1


async def get_all_shassis(
    session: AsyncSession,
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100,
):
    shassi = await session.execute(
        select(Shassi).options(selectinload(Shassi.car)).offset(offset).limit(limit),
    )
    return shassi.scalars().all()


async def get_shassi(
    shassi_id: int,
    session: AsyncSession = Depends(get_async_session),
):
    shassi = await session.get(Shassi, shassi_id)

    if not shassi:
        raise HTTPException(status_code=404, detail="Зип не найден")
    return shassi


async def delete_shassi(
    shassi_id: int,
    session: AsyncSession = Depends(get_async_session),
):
    shassi = await session.get(Shassi, shassi_id)

    if shassi is None:
        raise HTTPException(status_code=404, detail="Зип не найден")
    await session.delete(shassi)
    await session.commit()
    return {"success": True}
