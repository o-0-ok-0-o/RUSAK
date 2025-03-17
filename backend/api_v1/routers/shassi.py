from typing import Annotated
from fastapi import Query, APIRouter, Depends, UploadFile, File
from sqlalchemy.ext.asyncio import AsyncSession

from api_v1.crud.shassi import (
    create_shassi,
    get_shassi,
    get_all_shassis,
    delete_shassi,
    get_shassi_price,
)
from api_v1.schemas.shassi import ShassiBase, ShassiCar
from db.database import get_async_session

router = APIRouter(
    prefix="/shassi",
    tags=["Шасси"],
)


@router.post("", response_model=ShassiCar)
async def create_shassi_api(
    shassi: Annotated[ShassiBase, Depends()],
    file: UploadFile = File(),
    session: AsyncSession = Depends(get_async_session),
):
    shassi = await create_shassi(
        shassi=shassi,
        photo=file,
        session=session,
    )
    return shassi


#
@router.get("/{shassi_id}", response_model=ShassiBase)
async def get_shassi_api(
    shassi_id: int,
    session: AsyncSession = Depends(get_async_session),
):
    shassi = await get_shassi(shassi_id, session)
    return shassi


#
@router.get("", response_model=list[ShassiBase])
async def get_all_shassi_api(
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100,
    session: AsyncSession = Depends(get_async_session),
):
    shassis = await get_all_shassis(
        session,
        offset=offset,
        limit=limit,
    )
    return shassis


@router.get("/{shassi_id}/price")
async def get_shassi_price_api(
    shassi_id: int,
    session: AsyncSession = Depends(get_async_session),
):
    shassi_price = await get_shassi_price(shassi_id, session)
    return {"shassi_price": shassi_price}


@router.delete("/{shassi_id}")
async def delete_shassi_api(
    shassi_id: int,
    session: AsyncSession = Depends(get_async_session),
):
    shassi = await delete_shassi(shassi_id, session)
    return shassi
