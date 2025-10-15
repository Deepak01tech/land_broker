from fastapi import APIRouter, File, UploadFile
import shutil
from fastapi import Depends
from sqlalchemy.orm import Session
from src.db.database import SessionLocal
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.schemas.plot import PlotCreate, PlotOut
from src.models.plot import Plot
from src.db.database import get_db
from src.auth.jwthandler import get_current_user  # your JWT auth

# router = APIRouter()
router = APIRouter(prefix="/plots", tags=["Plots"])

@router.post("/", response_model=PlotOut)
def create_plot(plot: PlotCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    new_plot = Plot(**plot.dict(), owner_id=user.id)
    db.add(new_plot)
    db.commit()
    db.refresh(new_plot)
    return new_plot

@router.get("/", response_model=list[PlotOut])
def get_all_plots(db: Session = Depends(get_db)):
    return db.query(Plot).all()

@router.get("/{id}", response_model=PlotOut)
def get_plot(id: int, db: Session = Depends(get_db)):
    plot = db.query(Plot).filter(Plot.id == id).first()
    if not plot:
        raise HTTPException(status_code=404, detail="Plot not found")
    return plot

@router.put("/{id}", response_model=PlotOut)
def update_plot(id: int, plot_data: PlotCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    plot = db.query(Plot).filter(Plot.id == id).first()
    if not plot or plot.owner_id != user.id:
        raise HTTPException(status_code=403, detail="Unauthorized or plot not found")
    for key, value in plot_data.dict().items():
        setattr(plot, key, value)
    db.commit()
    db.refresh(plot)
    return plot

@router.delete("/{id}")
def delete_plot(id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    plot = db.query(Plot).filter(Plot.id == id).first()
    if not plot or plot.owner_id != user.id:
        raise HTTPException(status_code=403, detail="Unauthorized or plot not found")
    db.delete(plot)
    db.commit()
    return {"message": "Plot deleted successfully"}


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