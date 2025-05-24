# app/main.py

from fastapi import FastAPI
from app.db.createDB import CreateDB

app = FastAPI()

#Crear la base de datos
create_db = CreateDB()
create_db.crear_base_datos()

@app.get("/")
async def root():
    return {"message": "Bienvenido a la API de Login con FastAPI"}


# Iniciar la aplicación con el siguiente comando:
# uvicorn app.main:app --reload
