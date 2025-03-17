from fastapi import APIRouter, UploadFile, File

from utils.photo import create_photo

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
