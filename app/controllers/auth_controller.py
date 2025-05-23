# app/controllers/auth_controller.py

from fastapi import HTTPException, Depends
from app.services.auth_services import authenticate_user, create_user
from app.schemas.user import UserLogin, UserResponse
from app.core.security import manager
from app.db.database import get_user_collection
from fastapi import status
from bson.json_util import dumps
import json

@manager.user_loader
def load_user(username: str):
    user = authenticate_user(username, "")
    return user

def login(data: UserLogin):
    user = authenticate_user(data.username, data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Credenciales inválidas")
    access_token = manager.create_access_token(data={"sub": data.username})
    return {"access_token": access_token, "token_type": "bearer"}

def register(data: UserLogin):
    create_user(data.username, data.password)
    return UserResponse(username=data.username, message="Usuario registrado")

@manager.user_loader()
def get_users(current_user=Depends(manager)):
    users = list(get_user_collection().find())
    if not users:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No se encontraron usuarios"
        )
    # Convertir toda la lista en un string JSON válido
    return json.loads(dumps(users))