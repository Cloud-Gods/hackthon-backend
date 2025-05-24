# app/main.py

from fastapi import FastAPI
from app.db.createDB import CreateDB
from app.controllers.webScraping.conexion import ConexionPagina

app = FastAPI()

#Crear la base de datos
create_db = CreateDB()
create_db.crear_base_datos()

@app.get("/")
async def root():
    return {"message": "Bienvenido a la API de Login con FastAPI"}

@app.get("/GET/CaseNumber")
async def get_radicado(params):
    conexion = ConexionPagina()
    resultado = conexion.consultar_numeroRadicado(params)
    
    return resultado

@app.get("/GET/QueryName")
async def get_nombre(params):
    conexion = ConexionPagina()
    resultado = conexion.consultar_nombreRazonSocial(params)
    
    return resultado

@app.get("/GET/CaseDetail")
async def get_detalle(numero):
    conexion = ConexionPagina()
    resultado = conexion.consultar_detalleProceso(numero)
    
    return resultado

@app.get("/GET/ActuacionesProcess")
async def get_actuaciones(numero):
    conexion = ConexionPagina()
    resultado = conexion.consultar_actuacionesProcesoList(numero)
    
    return resultado






# Iniciar la aplicación con el siguiente comando:
# uvicorn app.main:app --reload
