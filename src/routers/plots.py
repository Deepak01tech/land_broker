from fastapi import APIRouter, File, UploadFile
import shutil
from fastapi import Depends
from sqlalchemy.orm import Session
from src.db.database import SessionLocal

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

@router.post("/plots/")
async def uploaddetailsofplot():
    return {"message": "Upload details of the plot here"}


@router.post("/upload-image/")
async def upload_image(file: UploadFile = File(...)):
    with open(f"static/uploads/{file.filename}", "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"filename": file.filename}

# @router.post("/upload_plot_details/")
# async def upload_plot_details(file: UploadFile = File(...), db: Session = Depends(get_db)):
#     with open(f"static/uploads/{file.filename}", "wb") as buffer:
#         shutil.copyfileobj(file.file, buffer)

#     # Here you would typically process the file and save details to the database
#     # For now, we just return the filename
#     return {"filename": file.filename}