from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from src.db.database import Base
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


    user = relationship("User", back_populates="plots")
    user_id = Column(Integer, ForeignKey("users.id"))