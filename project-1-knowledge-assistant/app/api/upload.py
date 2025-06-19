import shutil
from pathlib import Path

from fastapi import APIRouter, File, HTTPException, UploadFile
from fastapi.responses import JSONResponse
from app.ingestion.text_extract import extract_text_from_pdf

router = APIRouter()

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
ALLOWED_EXTENSIONS = {".pdf"}


@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    ext = Path(file.filename).suffix.lower()
    if ext not in ALLOWED_EXTENSIONS:
        raise HTTPException(status_code=400, detail="Only PDF file is allowed")

    file_path = UPLOAD_DIR / file.filename
    try:
        with file_path.open("wb") as f:
            shutil.copyfileobj(file.file, f)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"File save failed: {str(e)}")
    text = extract_text_from_pdf(file_path=file_path)
    return JSONResponse(
        status_code=200,
        content={
            "message": "File uploaded successfully.",
            "filename": file.filename,
            "extracted_text": text,
        },
    )
