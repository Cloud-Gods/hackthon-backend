# app/main.py

from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from app.db.createDB import CreateDB
from app.controllers.ApiJuridica.conexion import ConexionPagina

app = FastAPI()

# Lista de orígenes permitidos (puedes ajustarlo según tus necesidades)
origins = [
    "http://localhost:3000",
    "http://192.168.1.16:3000", 
]

# Middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#Crear la base de datos
create_db = CreateDB()
create_db.crear_base_datos()

@app.get("/")
async def root():
    return {"message": "Bienvenido a la API de Login con FastAPI"}

@app.get("/GET/CaseNumber")
async def get_radicado(
    numero: str = Query(..., alias="numero"),         
    SoloActivos: bool = Query(True, alias="SoloActivos"), 
    pagina: int = Query(1, alias="pagina")            
):
    params = {
        "Numero": numero,
        "SoloActivos": SoloActivos,
        "pagina": pagina
    }
    conexion = ConexionPagina()
    resultado = conexion.consultar_numeroRadicado(params)
    
    return resultado

@app.get("/GET/QueryName")
async def get_nombre():
    params = {
    "Nombre": "Juan Perez",              # Nombre completo
    "SoloActivos": "false",              # (opcional) si quieres ver solo los activos
    "pagina": 1                          # Página de resultados (paginación)
}
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
