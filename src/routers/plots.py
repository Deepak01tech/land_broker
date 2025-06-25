from fastapi import APIRouter, File, UploadFile
import shutil
from fastapi import Depends
from sqlalchemy.orm import Session
from db.database import SessionLocal

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/")
async def read_root():
    return {"message": "Welcome to the Land Broker API"}


@router.post("/upload-image/")
async def upload_image(file: UploadFile = File(...)):
    with open(f"static/uploads/{file.filename}", "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"filename": file.filename}
