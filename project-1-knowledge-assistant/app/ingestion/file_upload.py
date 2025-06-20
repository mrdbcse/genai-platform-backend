import os
import shutil
from uuid import uuid4

from fastapi import UploadFile

UPLOAD_DIR = "uploaded_docs"
os.makedirs(UPLOAD_DIR, exist_ok=True)


def save_file(file: UploadFile) -> str:
    file_extension = os.path.splitext(file.filename)[-1]
    if file_extension not in [".pdf", ".docx"]:
        raise ValueError("Unsupported file type")

    file_id = f"{uuid4().hex}{file_extension}"
    file_path = os.path.join(UPLOAD_DIR, file_id)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return file_path
