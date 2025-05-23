# app/routers/auth.py

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from app.controllers.auth_controller import login, register
from app.schemas.user import UserLogin
from app.core.security import manager
from app.controllers.auth_controller import get_users


router = APIRouter()

@router.post("/login")
async def login_user(form_data: OAuth2PasswordRequestForm = Depends()):
    data = UserLogin(username=form_data.username, password=form_data.password)
    return login(data)

@router.post("/register")
async def register_user(data: UserLogin):
    return register(data)

@router.get("/users", summary="Consultar usuarios", dependencies=[Depends(manager)])
async def get_all_users(current_user=Depends(manager)):
    return get_users()