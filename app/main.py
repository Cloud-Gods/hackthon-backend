# app/main.py

from fastapi import FastAPI
from app.routers import auth
from app.db.createDB import CreateDB

app = FastAPI()
#Crear la base de datos
create_db = CreateDB()
create_db.crear_base_datos()

@app.get("/")
async def root():
    return {"message": "Bienvenido a la API de Login con FastAPI"}

# Incluyendo el router de autenticación
app.include_router(auth.router, prefix="/auth")

# Iniciar la aplicación con el siguiente comando:
# uvicorn app.main:app --reload
