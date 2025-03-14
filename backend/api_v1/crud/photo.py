from io import BytesIO

from PIL import Image
from fastapi import FastAPI, UploadFile, File, HTTPException
import os
import uuid

from config import UPLOAD_DIR


async def create_photo(
        file: UploadFile
):
    if not file.content_type.startswith("image/"):
        raise HTTPException(400, "Invalid file type")

    file_ext = file.filename.split(".")[-1]
    filename = f"{uuid.uuid4()}.{file_ext}"
    file_path = os.path.join(UPLOAD_DIR, filename)

    try:
        contents = await file.read()

        image = Image.open(BytesIO(contents))
        image.thumbnail((800, 800))
        image.save(file_path)
    except Exception:
        raise HTTPException(500, "Could not save file")

    photo_url=f"/test-photo/{filename}"

    return photo_url