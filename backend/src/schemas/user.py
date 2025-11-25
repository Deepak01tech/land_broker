from pydantic import BaseModel, EmailStr
from typing import Optional

# Schema for creating a new user
class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str

# Schema for displaying user details (response model)
class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr

    class Config:
        orm_mode = True  # allows returning SQLAlchemy objects directly
