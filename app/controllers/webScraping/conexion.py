import requests
from bs4 import BeautifulSoup
import sys
import os
sys.path.append("c:/Users/yeiso/OneDrive/Escritorio/Proyecto/TalentoTech/Hackathon/hackthon-backend")
from app.models.logger import Logger

#Clase para manejar la conexicon con la pagina web
class ConexionPagina:
    def __init__(self):
        self.url = "https://consultaprocesos.ramajudicial.gov.co/procesos/Index"
        self.log = Logger("logs/Conexion.log").get_logger()
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

    #Funcion para conectar a la pagina web
    def conectar(self):
        try:
            response = requests.get(self.url, headers=self.headers)
            if response.status_code == 200:
                self.log.info("Conexión exitosa a la página web")
                return response
            else:
                self.log.warning(f"Error al conectar a la pagina web: {response.status_code}")
        except Exception as ex:
            self.log.error(f"Error al conectar a la pagina web: {ex}")

ConexionPagina().conectar()