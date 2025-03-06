from fastapi import Depends, Query, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from typing import Annotated
from api_v1.schemas.schemas import SaloneMemberBase
from db.database import get_async_session
from db.models import SaloneMember, SaloneOption


async def create_salone_option(
    salone_option: Annotated[SaloneMemberBase, Depends()],
    session: AsyncSession = Depends(get_async_session),
):
    salone_option_dict: dict = salone_option.model_dump()
    salone_option_model = SaloneOption(**salone_option_dict)
    session.add(salone_option_model)
    await session.commit()
    return salone_option


async def get_all_salone_options(
    session: AsyncSession,  # = Depends(get_async_session),
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100,
):
    salone_option = await session.execute(
        select(SaloneOption)
        .options(selectinload(SaloneOption.car))
        .offset(offset)
        .limit(limit),
    )
    return salone_option.scalars().all()


async def get_salone_option(
    salone_option_id: int,
    session: AsyncSession = Depends(get_async_session),
):
    salone_option = await session.get(SaloneOption, salone_option_id)

    if not salone_option:
        raise HTTPException(status_code=404, detail="Опция салона не найдена")
    return salone_option


async def delete_salone_option(
    salone_option_id: int,
    session: AsyncSession = Depends(get_async_session),
):
    salone_option = await session.get(SaloneOption, salone_option_id)

    if salone_option is None:
        raise HTTPException(status_code=404, detail="Опция салона не найденоа")
    await session.delete(salone_option)
    await session.commit()
    return {"success": True}
