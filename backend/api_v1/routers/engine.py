from typing import Annotated
from fastapi import HTTPException, Query, APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from api_v1.crud.engine import (
    create_engine,
    get_engine,
    get_all_engines,
    delete_engine,
    get_engine_price,
)
from api_v1.schemas.schemas import EngineBase
from db.database import get_async_session


router = APIRouter(
    prefix="/engines",
    tags=["Двигатели"],
)


@router.post("", response_model=EngineBase)
async def create_engine_api(
    engine: Annotated[EngineBase, Depends()],
    session: AsyncSession = Depends(get_async_session),
):
    engine = await create_engine(engine, session)
    return engine


#
@router.get("/{engine_id}", response_model=EngineBase)
async def get_engine_api(
    engine_id: int,
    session: AsyncSession = Depends(get_async_session),
):
    engine = await get_engine(engine_id, session)
    return engine


#
@router.get("", response_model=list[EngineBase])
async def get_all_engine_api(
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100,
    session: AsyncSession = Depends(get_async_session),
):
    engines = await get_all_engines(
        session,
        offset=offset,
        limit=limit,
    )
    return engines


@router.get("/{engine_id}/price")
async def get_engine_price_api(
    engine_id: int,
    session: AsyncSession = Depends(get_async_session),
):
    engine_price = await get_engine_price(engine_id, session)
    return {"engine_price": engine_price}


@router.delete("/{engine_id}")
async def delete_engine_api(
    engine_id: int,
    session: AsyncSession = Depends(get_async_session),
):
    engine = await delete_engine(engine_id, session)
    return engine
