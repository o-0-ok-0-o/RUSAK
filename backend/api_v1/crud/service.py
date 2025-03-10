from fastapi import Depends, Query, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from typing import Annotated
from api_v1.schemas.schemas import SaloneMemberBase, ServiceBase
from db.database import get_async_session
from db.models import Service


async def create_service(
    service: Annotated[ServiceBase, Depends()],
    session: AsyncSession = Depends(get_async_session),
):
    service_dict: dict = service.model_dump()
    service_model = Service(**service_dict)
    session.add(service_model)
    await session.commit()
    return service


async def get_all_services(
    session: AsyncSession,
    offset: int = 0,
    limit: int = 100,
):
    service = await session.execute(
        select(Service).options(selectinload(Service.car)).offset(offset).limit(limit),
    )
    return service.scalars().all()


async def get_service(
    service_id: int,
    session: AsyncSession = Depends(get_async_session),
):
    service = await session.get(Service, service_id)

    if not service:
        raise HTTPException(status_code=404, detail="Сервис не найден")
    return service


async def get_service_price(
    service_id: int,
    session: AsyncSession = Depends(get_async_session),
):
    result = await session.execute(
        select(Service.base_price).where(Service.id == service_id)
    )

    service_price = result.scalar()

    if not service_price:
        raise HTTPException(status_code=404, detail="Сервис не найден")
    return service_price


async def delete_service(
    service_id: int,
    session: AsyncSession = Depends(get_async_session),
):
    service = await session.get(Service, service_id)

    if service is None:
        raise HTTPException(status_code=404, detail="Сервис не найден")
    await session.delete(service)
    await session.commit()
    return {"success": True}
