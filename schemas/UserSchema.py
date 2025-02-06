from pydantic import BaseModel, EmailStr, validator
import re

class UserBase(BaseModel):
    name: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

    @validator("password")
    def validate_password(cls, value):
        if len(value) < 8:
            raise ValueError("Password must be at least 8 characters long")
        if not re.search(r"[A-Za-z]", value):
            raise ValueError("Password must contain at least one letter")
        if not re.search(r"[0-9]", value):
            raise ValueError("Password must contain at least one number")
        return value

class UserResponse(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True
