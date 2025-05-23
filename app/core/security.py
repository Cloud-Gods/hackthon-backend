# app/core/security.py

from fastapi_login import LoginManager
import os
from dotenv import load_dotenv
from app.services.auth_services import authenticate_user

load_dotenv()

SECRET = os.getenv("SECRET_KEY")
manager = LoginManager(SECRET, token_url="/auth/login")