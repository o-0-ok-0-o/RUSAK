from typing import Annotated
from fastapi import HTTPException, Query, APIRouter, Depends, UploadFile, File
from sqlalchemy.ext.asyncio import AsyncSession

from api_v1.crud.salone_member import (
    create_salone_member,
    get_salone_member,
    get_all_salone_members,
    get_salone_member_price,
    delete_salone_member,
)
from api_v1.schemas.salone_member import SaloneMemberBase, SaloneMemberCar
from db.database import get_async_session


router = APIRouter(
    prefix="/salone-member",
    tags=["Салон кол-во"],
)


@router.post("", response_model=SaloneMemberCar)
async def create_salone_member_api(
    salone_member: Annotated[SaloneMemberBase, Depends()],
    file: UploadFile = File(),
    session: AsyncSession = Depends(get_async_session),
):
    salone_member = await create_salone_member(
        salone_member=salone_member,
        photo=file,
        session=session,
    )
    return salone_member


@router.get("/{salone_member_id}", response_model=SaloneMemberBase)
async def get_salone_member_api(
    salone_member_id: int,
    session: AsyncSession = Depends(get_async_session),
):
    salone_member = await get_salone_member(salone_member_id, session)
    return salone_member


@router.get("", response_model=list[SaloneMemberBase])
async def get_all_salone_member_api(
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100,
    session: AsyncSession = Depends(get_async_session),
):
    salone_members = await get_all_salone_members(
        session,
        offset=offset,
        limit=limit,
    )
    return salone_members


@router.get("/{salone_member_id}/price")
async def get_salone_member_price_api(
    salone_member_id: int,
    session: AsyncSession = Depends(get_async_session),
):
    salone_member_price = await get_salone_member_price(salone_member_id, session)
    return {"salone_member_price": salone_member_price}


@router.delete("/{salone_member_id}")
async def delete_salone_member_api(
    salone_member_id: int,
    session: AsyncSession = Depends(get_async_session),
):
    salone_member = await delete_salone_member(salone_member_id, session)
    return salone_member
