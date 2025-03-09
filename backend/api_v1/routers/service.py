from typing import Annotated
from fastapi import Query, APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api_v1.crud.service import (
    create_service,
    get_service,
    get_all_services,
    delete_service,
    get_service_price,
)
from api_v1.schemas.schemas import ServiceBase
from db.database import get_async_session

router = APIRouter(
    prefix="/service",
    tags=["Сервис"],
)


@router.post("", response_model=ServiceBase)
async def create_service_api(
    service: Annotated[ServiceBase, Depends()],
    session: AsyncSession = Depends(get_async_session),
):
    service = await create_service(service, session)
    return service


#
@router.get("/{service_id}", response_model=ServiceBase)
async def get_service_api(
    service_id: int,
    session: AsyncSession = Depends(get_async_session),
):
    service = await get_service(service_id, session)
    return service


#
@router.get("", response_model=list[ServiceBase])
async def get_all_service_api(
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100,
    session: AsyncSession = Depends(get_async_session),
):
    services = await get_all_services(
        session,
        offset=offset,
        limit=limit,
    )
    return services


@router.get("/{service_id}/price")
async def get_service_price_api(
    service_id: int,
    session: AsyncSession = Depends(get_async_session),
):
    service_price = await get_service_price(service_id, session)
    return {"service_price": service_price}


@router.delete("/{service_id}")
async def delete_service_api(
    service_id: int,
    session: AsyncSession = Depends(get_async_session),
):
    service = await delete_service(service_id, session)
    return service
