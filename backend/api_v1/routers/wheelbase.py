from typing import Annotated
from fastapi import HTTPException, Query, APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from api_v1.crud.wheelbase import (
    create_wheelbase,
    get_wheelbase,
    get_all_wheelbases,
    delete_wheelbase,
    get_wheelbase_price,
)
from api_v1.schemas.wheelbase import WheelbaseBase
from db.database import get_async_session


router = APIRouter(
    prefix="/wheelbases",
    tags=["Двигатели"],
)


@router.post("", response_model=WheelbaseBase)
async def create_wheelbase_api(
    wheelbase: Annotated[WheelbaseBase, Depends()],
    session: AsyncSession = Depends(get_async_session),
):
    wheelbase = await create_wheelbase(wheelbase, session)
    return wheelbase


#
@router.get("/{wheelbase_id}", response_model=WheelbaseBase)
async def get_wheelbase_api(
    wheelbase_id: int,
    session: AsyncSession = Depends(get_async_session),
):
    wheelbase = await get_wheelbase(wheelbase_id, session)
    return wheelbase


#
@router.get("", response_model=list[WheelbaseBase])
async def get_all_wheelbase_api(
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100,
    session: AsyncSession = Depends(get_async_session),
):
    wheelbases = await get_all_wheelbases(
        session,
        offset=offset,
        limit=limit,
    )
    return wheelbases


@router.get("/{wheelbase_id}/price")
async def get_wheelbase_price_api(
    wheelbase_id: int,
    session: AsyncSession = Depends(get_async_session),
):
    wheelbase_price = await get_wheelbase_price(wheelbase_id, session)
    return {"wheelbase_price": wheelbase_price}


@router.delete("/{wheelbase_id}")
async def delete_wheelbase_api(
    wheelbase_id: int,
    session: AsyncSession = Depends(get_async_session),
):
    wheelbase = await delete_wheelbase(wheelbase_id, session)
    return wheelbase
