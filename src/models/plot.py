
from typing import Optional
from pydantic import BaseModel


class PlotBase(BaseModel):
    title: str
    location: str
    size: float
    price: float
    description: Optional[str] = None

class PlotCreate(PlotBase):
    pass

class PlotOut(PlotBase):
    id: int
    owner_id: int
