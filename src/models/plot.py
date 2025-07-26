from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from db.database import Base
from typing import Optional
from pydantic import BaseModel





class Plot(Base):
    __tablename__ = "plots"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))
    location = Column(String(255))
    price = Column(Float)
    size = Column(Float)
    description = Column(String(500))
    image = Column(String(255), nullable=True)

    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="plots")
