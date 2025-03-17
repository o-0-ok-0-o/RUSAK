from typing import Annotated
from fastapi import HTTPException, Query, APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from api_v1.crud.tire import (
    create_tire,
    get_tire,
    get_all_tires,
    delete_tire,
    get_tire_price,
)
from api_v1.schemas.tire import TireBase
from db.database import get_async_session


router = APIRouter(
    prefix="/tires",
    tags=["Шины"],
)


@router.post("", response_model=TireBase)
async def create_tire_api(
    tire: Annotated[TireBase, Depends()],
    session: AsyncSession = Depends(get_async_session),
):
    tire = await create_tire(tire, session)
    return tire


#
@router.get("/{tire_id}", response_model=TireBase)
async def get_tire_api(
    tire_id: int,
    session: AsyncSession = Depends(get_async_session),
):
    tire = await get_tire(tire_id, session)
    return tire


#
@router.get("", response_model=list[TireBase])
async def get_all_tire_api(
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100,
    session: AsyncSession = Depends(get_async_session),
):
    tires = await get_all_tires(
        session,
        offset=offset,
        limit=limit,
    )
    return tires


@router.get("/{tire_id}/price")
async def get_tire_price_api(
    tire_id: int,
    session: AsyncSession = Depends(get_async_session),
):
    tire_price = await get_tire_price(tire_id, session)
    return {"tire_price": tire_price}


@router.delete("/{tire_id}")
async def delete_tire_api(
    tire_id: int,
    session: AsyncSession = Depends(get_async_session),
):
    tire = await delete_tire(tire_id, session)
    return tire
