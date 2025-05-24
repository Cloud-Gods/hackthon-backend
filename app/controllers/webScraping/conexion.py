import requests
from bs4 import BeautifulSoup
import json
import sys
sys.path.append("c:/Users/yeiso/OneDrive/Escritorio/Proyecto/TalentoTech/Hackathon/hackthon-backend")
from app.models.logger import Logger

#Clase para manejar la conexicon con la pagina web
class ConexionPagina:
    def __init__(self):
        self.url = "https://consultaprocesos.ramajudicial.gov.co/procesos/Index"
        self.log = Logger("logs/ObtenerDatos.log").get_logger()
        self.headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/113.0.0.0 Safari/537.36"
            ),
            "Accept-Language": "es-ES,es;q=0.9",
            "Referer": "https://consultaprocesos.ramajudicial.gov.co/",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
        }

    #Funcion para ir a la pagina de consulta por numero de radicado
    def consultar_numeroRadicado(self,parametros):
        self.url = "https://consultaprocesos.ramajudicial.gov.co:448/api/v2/Procesos/Consulta/NumeroRadicacion"
        try:
            response = requests.get(self.url,params=parametros, headers=self.headers)
            #Si la respuesta es exitosa, se devuelve el json
            if response.status_code == 200:
                self.log.info("Conexión exitosa a la página de consulta por número de radicado")
                return response.json()
            #En caso de que no sea asi, se devuelve un mensaje de error
            else:
                self.log.warning(f"Error al conectar a la pagina web: {response.status_code}")
        except Exception as ex:
            self.log.error(f"Error al conectar a la pagina web: {ex}")

    #FUncion para consultar por nombre, departamento y ciudad
    def consultar_nombreRazonSocial(self, parametros):
        url = "https://consultaprocesos.ramajudicial.gov.co:448/api/v2/Procesos/Consulta/NombreRazonSocial"
        procesos_list = []
        try:
            response = requests.get(url, params=parametros, headers=self.headers)
            if response.status_code != 200:
                self.log.error(f"Error en la página {parametros['pagina']}: {response.status_code}")
                return []

            data = response.json()
            procesos = data.get("procesos", [])
            procesos_list.extend(procesos)

            pagina_actual = data.get("paginacion", {}).get("pagina", 1)
            total_paginas = data.get("paginacion", {}).get("cantidadPaginas", 1)

            print(f"Página {pagina_actual} de {total_paginas} descargada.")
            self.log.info(f"{procesos_list}")
            self.log.info(f"Procesos encontrados en esta página: {len(procesos_list)}")

            return procesos_list

        except Exception as ex:
            self.log.error(f"Error al conectar a la pagina web: {ex}")
            return []

    #Funcion para consultar detalle de un proceso
    def consultar_detalleProceso(self,parametros):
        self.url = "https://consultaprocesos.ramajudicial.gov.co:448/api/v2/Procesos/Consulta/Detalle"
        try:
            response = requests.get(self.url,params=parametros, headers=self.headers)
            #Si la respuesta es exitosa, se devuelve el json
            if response.status_code == 200:
                self.log.info("Conexión exitosa a la página de consulta por número de radicado")
                return response.json()
            #En caso de que no sea asi, se devuelve un mensaje de error
            else:
                self.log.warning(f"Error al conectar a la pagina web: {response.status_code}")
        except Exception as ex:
            self.log.error(f"Error al conectar a la pagina web: {ex}")

ConexionPagina().consultar_nombreRazonSocial(
    parametros = {
    "nombre": "Falabella",
    "tipoPersona": "jur",               
    "SoloActivos": "true",
    "codificacionDespacho": "05001",   
    "pagina": 1
    }
)