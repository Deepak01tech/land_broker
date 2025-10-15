from pydantic import BaseModel
from typing import Optional

class PlotBase(BaseModel):
    title: str
    location: str
    price: float
    size: float
    description: Optional[str] = None

class PlotCreate(PlotBase):
    pass

class PlotOut(PlotBase):
    id: int
    owner_id: int
    image: Optional[str]

    class Config:
        orm_mode = True
