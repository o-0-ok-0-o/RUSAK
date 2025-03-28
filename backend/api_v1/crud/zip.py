from fastapi import Depends, Query, HTTPException, UploadFile
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from typing import Annotated
from api_v1.schemas.zip import ZipBase
from db.database import get_async_session
from db.models import Zip
from utils.photo import create_photo


async def create_zip(
    zip1: ZipBase,
    photo: UploadFile,
    session: AsyncSession = Depends(get_async_session),
):
    try:
        file_path = await create_photo(photo)
        zip_dict: dict = zip1.model_dump()
        zip_dict['photo_url'] = file_path
        zip_model = Zip(**zip_dict)

        session.add(zip_model)
        await session.commit()
        await session.refresh(zip_model)
        return zip_model
    except Exception as e:
        await session.rollback()  # Откатываем транзакцию в случае ошибки
        raise e  # Повторно поднимаем исключение для обработки на уровне выше



async def get_all_zips(
    session: AsyncSession,
    offset: int = 0,
    limit:int = 100,
):
    zip1 = await session.execute(
        select(Zip).options(selectinload(Zip.car)).offset(offset).limit(limit),
    )
    return zip1.scalars().all()


async def get_zip(
    zip_id: int,
    session: AsyncSession = Depends(get_async_session),
):
    zip1 = await session.get(Zip, zip_id)

    if not zip1:
        raise HTTPException(status_code=404, detail="Зип не найден")
    return zip1


async def get_zip_price(
    zip_id: int,
    session: AsyncSession = Depends(get_async_session),
):
    result = await session.execute(select(Zip.base_price).where(Zip.id == zip_id))

    zip_price = result.scalar()

    if not zip_price:
        raise HTTPException(status_code=404, detail="Зип не найден")
    return zip_price


async def delete_zip(
    zip_id: int,
    session: AsyncSession = Depends(get_async_session),
):
    zip1 = await session.get(Zip, zip_id)

    if zip1 is None:
        raise HTTPException(status_code=404, detail="Зип не найден")
    await session.delete(zip1)
    await session.commit()
    return {"success": True}
