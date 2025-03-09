from typing import Annotated
from fastapi import Query, APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api_v1.crud.zip import (
    create_zip,
    get_zip,
    get_all_zips,
    delete_zip,
    get_zip_price,
)
from api_v1.schemas.schemas import ZipBase
from db.database import get_async_session

router = APIRouter(
    prefix="/zip",
    tags=["Зип"],
)


@router.post("", response_model=ZipBase)
async def create_zip_api(
    zip1: Annotated[ZipBase, Depends()],
    session: AsyncSession = Depends(get_async_session),
):
    zip1 = await create_zip(zip1, session)
    return zip1


#
@router.get("/{zip_id}", response_model=ZipBase)
async def get_zip1_api(
    zip_id: int,
    session: AsyncSession = Depends(get_async_session),
):
    zip1 = await get_zip(zip_id, session)
    return zip1


#
@router.get("", response_model=list[ZipBase])
async def get_all_zip_api(
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100,
    session: AsyncSession = Depends(get_async_session),
):
    zips = await get_all_zips(
        session,
        offset=offset,
        limit=limit,
    )
    return zips


@router.get("/{zip_id}/price")
async def get_zip_price_api(
    zip_id: int,
    session: AsyncSession = Depends(get_async_session),
):
    zip1_price = await get_zip_price(zip_id, session)
    return {"zip_price": zip1_price}


@router.delete("/{zip_id}")
async def delete_zip1_api(
    zip_id: int,
    session: AsyncSession = Depends(get_async_session),
):
    zip1 = await delete_zip(zip_id, session)
    return zip1
