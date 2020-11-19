from typing import Optional

from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    email: str = None
    full_name: Optional[str] = None
    disabled: Optional[bool] = None


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int

    class Config:
        orm_mode = True
