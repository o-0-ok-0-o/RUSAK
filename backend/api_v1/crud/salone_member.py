from fastapi import Depends, Query, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from typing import Annotated
from api_v1.schemas.salone_member import SaloneMemberBase
from db.database import get_async_session
from db.models import SaloneMember


async def create_salone_member(
    salone_member: Annotated[SaloneMemberBase, Depends()],
    session: AsyncSession = Depends(get_async_session),
):
    salone_member_dict: dict = salone_member.model_dump()
    salone_member_model = SaloneMember(**salone_member_dict)
    session.add(salone_member_model)
    await session.commit()
    return salone_member


async def get_all_salone_members(
    session: AsyncSession,  # = Depends(get_async_session),
    offset: int = 0,
    limit: int = 100,
):
    salone_member = await session.execute(
        select(SaloneMember)
        .options(selectinload(SaloneMember.cars))
        .offset(offset)
        .limit(limit),
    )
    return salone_member.scalars().all()


async def get_salone_member(
    salone_member_id: int,
    session: AsyncSession = Depends(get_async_session),
):
    salone_member = await session.get(SaloneMember, salone_member_id)

    if not salone_member:
        raise HTTPException(status_code=404, detail="Кол-во мест не найден")
    return salone_member


async def get_salone_member_price(
    salone_member_id: int,
    session: AsyncSession = Depends(get_async_session),
):
    result = await session.execute(
        select(SaloneMember.base_price).where(SaloneMember.id == salone_member_id)
    )

    salone_member_price = result.scalar()

    if not salone_member_price:
        raise HTTPException(status_code=404, detail="Кол-во мест не найден")
    return salone_member_price


async def delete_salone_member(
    salone_member_id: int,
    session: AsyncSession = Depends(get_async_session),
):
    salone_member = await session.get(SaloneMember, salone_member_id)

    if salone_member is None:
        raise HTTPException(status_code=404, detail="Кол-во мест не найдено")
    await session.delete(salone_member)
    await session.commit()
    return {"success": True}
