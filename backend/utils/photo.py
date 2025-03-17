from fastapi import UploadFile
from config import UPLOAD_DIR
import os
import uuid
import aiofiles

async def create_photo(file: UploadFile):
    file_extension = os.path.splitext(file.filename)[1]
    unique_filename = f"{uuid.uuid4()}{file_extension}"
    file_location = f"{UPLOAD_DIR}/{unique_filename}"

    async with aiofiles.open(file_location, "wb") as file_object:
        content = await file.read()
        await file_object.write(content)

    return file_location
