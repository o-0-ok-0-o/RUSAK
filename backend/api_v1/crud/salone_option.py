from fastapi import Depends, Query, HTTPException, UploadFile
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from typing import Annotated
from api_v1.schemas.salone_option import SaloneOptionBase
from db.database import get_async_session
from db.models import SaloneOption
from utils.photo import create_photo


async def create_salone_option(
    salone_option: SaloneOptionBase,
    photo: UploadFile,
    session: AsyncSession = Depends(get_async_session),
):
    try:
        file_path = await create_photo(photo)
        salone_option_dict: dict = salone_option.model_dump()
        salone_option_dict["photo_url"] = file_path
        salone_option_model = SaloneOption(**salone_option_dict)

        session.add(salone_option_model)
        await session.commit()
        await session.refresh(salone_option_model)
        return salone_option_model
    except Exception as e:
        await session.rollback()  # Откатываем транзакцию в случае ошибки
        raise e  # Повторно поднимаем исключение для обработки на уровне выше


async def get_all_salone_options(
    session: AsyncSession,  # = Depends(get_async_session),
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100,
):
    salone_option = await session.execute(
        select(SaloneOption)
        .options(selectinload(SaloneOption.car))
        .offset(offset)
        .limit(limit),
    )
    return salone_option.scalars().all()


async def get_salone_option(
    salone_option_id: int,
    session: AsyncSession,
):
    salone_option = await session.get(SaloneOption, salone_option_id)

    if not salone_option:
        raise HTTPException(status_code=404, detail="Опция салона не найдена")
    return salone_option


async def get_salone_option_price(
    salone_option_id: int,
    session: AsyncSession = Depends(get_async_session),
):
    result = await session.execute(
        select(SaloneOption.base_price).where(SaloneOption.id == salone_option_id)
    )

    salone_option_price = result.scalar()

    if not salone_option_price:
        raise HTTPException(status_code=404, detail="Опция салона не найдена")
    return salone_option_price


async def delete_salone_option(
    salone_option_id: int,
    session: AsyncSession = Depends(get_async_session),
):
    salone_option = await session.get(SaloneOption, salone_option_id)

    if salone_option is None:
        raise HTTPException(status_code=404, detail="Опция салона не найдено")
    await session.delete(salone_option)
    await session.commit()
    return {"success_delete": True}
