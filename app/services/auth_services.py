# app/services/auth_service.py

from app.utils.hashing import hash_password, verify_password
from app.db.database import get_user_collection

def create_user(username: str, password: str):
    user_collection = get_user_collection()
    hashed_password = hash_password(password)
    user = {"username": username, "password": hashed_password}
    user_collection.insert_one(user)

def authenticate_user(username: str, password: str):
    user_collection = get_user_collection()
    user = user_collection.find_one({"username": username})
    if user and verify_password(password, user["password"]):
        return user
    return None
