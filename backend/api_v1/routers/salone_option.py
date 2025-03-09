from typing import Annotated
from fastapi import Query, APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api_v1.crud.salone_option import (
    create_salone_option,
    get_salone_option,
    get_all_salone_options,
    delete_salone_option,
    get_salone_option_price,
)
from api_v1.schemas.schemas import SaloneOptionBase
from db.database import get_async_session

router = APIRouter(
    prefix="/salone-option",
    tags=["Опции салона"],
)


@router.post("", response_model=SaloneOptionBase)
async def create_salone_option_api(
    salone_option: Annotated[SaloneOptionBase, Depends()],
    session: AsyncSession = Depends(get_async_session),
):
    salone_option = await create_salone_option(salone_option, session)
    return salone_option


#
@router.get("/{salone_option_id}", response_model=SaloneOptionBase)
async def get_salone_option_api(
    salone_option_id: int,
    session: AsyncSession = Depends(get_async_session),
):
    salone_option = await get_salone_option(salone_option_id, session)
    return salone_option


#
@router.get("", response_model=list[SaloneOptionBase])
async def get_all_salone_option_api(
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100,
    session: AsyncSession = Depends(get_async_session),
):
    salone_options = await get_all_salone_options(
        session,
        offset=offset,
        limit=limit,
    )
    return salone_options


@router.get("/{salone_option_id}/price")
async def get_salone_option_price_api(
    salone_option_id: int,
    session: AsyncSession = Depends(get_async_session),
):
    salone_option_price = await get_salone_option_price(salone_option_id, session)
    return {"salone_option_price": salone_option_price}


@router.delete("/{salone_option_id}")
async def delete_salone_option_api(
    salone_option_id: int,
    session: AsyncSession = Depends(get_async_session),
):
    salone_option = await delete_salone_option(salone_option_id, session)
    return salone_option
