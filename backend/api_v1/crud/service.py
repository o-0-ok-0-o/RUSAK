from fastapi import Depends, Query, HTTPException, UploadFile
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from typing import Annotated
from api_v1.schemas.service import ServiceBase
from api_v1.schemas.salone_member import SaloneMemberBase
from db.database import get_async_session
from db.models import Service
from utils.photo import create_photo


async def create_service(
    service: ServiceBase,
    photo: UploadFile,
    session: AsyncSession = Depends(get_async_session),
):
    try:
        file_path = await create_photo(photo)
        service_dict: dict = service.model_dump()
        service_dict["photo_url"] = file_path
        service_model = Service(**service_dict)

        session.add(service_model)
        await session.commit()
        await session.refresh(service_model)
        return service_model
    except Exception as e:
        await session.rollback()  # Откатываем транзакцию в случае ошибки
        raise e  # Повторно поднимаем исключение для обработки на уровне выше


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
