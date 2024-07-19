from typing import Optional
from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    email: str
    password: str


class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None

class UserDisplay(BaseModel):
    id: int
    username: str
    email: str
    
    class Config:
        orm_mode=True