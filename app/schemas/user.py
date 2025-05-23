# app/schemas/user.py

from pydantic import BaseModel

class UserLogin(BaseModel):
    username: str
    password: str

class UserResponse(BaseModel):
    username: str
    message: str
