from typing import Annotated
from fastapi import APIRouter, Depends, UploadFile, File
from sqlalchemy.ext.asyncio import AsyncSession

from api_v1.crud.photo import create_photo
from db.database import get_async_session


router = APIRouter(
    prefix="/photo-upload-test",
    tags=["Загрузка фото тест"],
)


@router.post("")
async def create_engine_api(
    file: UploadFile = File(...),
):
    photo = await create_photo(file=file)
    return photo