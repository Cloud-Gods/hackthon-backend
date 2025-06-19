import requests
import json
import sys
sys.path.append("c:/Users/yeiso/OneDrive/Escritorio/Proyecto/TalentoTech/Hackathon/hackthon-backend")
from app.models.logger import Logger
from app.controllers.IA.conexionIA import ConexionIA
from app.utils.utils import Utils

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
                data = response.json()

                #Extraigo el tipo de proceso
                idProceso = data['procesos'][0]['idProceso']
                #Y se lo mando para que me devuleva la clase del proceso
                clase_proceso = self.obtener_tipoProceso(idProceso)
                #Ahora remplazo el tipo de proceso en la respuesta
                data['parametros']['claseProceso'] = clase_proceso.get('clase_proceso')

                self.log.info(f"datos: {data}")

                
                return data
            #En caso de que no sea asi, se devuelve un mensaje de error
            else:
                self.log.warning(f"Error al conectar a la pagina web: {response.status_code}")
        except Exception as ex:
            self.log.error(f"Error al conectar a la pagina web: {ex}")

    def consultar_nombreRazonSocial(self, parametros):
        self.url = "https://consultaprocesos.ramajudicial.gov.co:448/api/v2/Procesos/Consulta/NombreRazonSocial"
        try:
            response = requests.get(self.url, params=parametros, headers=self.headers)
            if response.status_code != 200:
                self.log.error(f"Error en la página {parametros['pagina']}: {response.status_code}")
                return [], 0

            data = response.json()
            procesos = data.get("procesos", [])

            # Para cada proceso, obtener y añadir la clase de proceso
            for proceso in procesos:
                idProceso = proceso.get('idProceso')
                if idProceso:
                    clase_proceso = self.obtener_tipoProceso(idProceso)
                    # Añadir la clase de proceso dentro del proceso
                    proceso['claseProceso'] = clase_proceso.get('clase_proceso')

            paginacion = data.get("paginacion", {})
            total_procesos = paginacion.get("cantidadRegistros", 0)


            resultado = {
                "total_procesos": total_procesos,
                "procesos": procesos,
            }
            self.log.info(f"Consulta exitosa: {resultado}")

            return json.dumps(resultado)

        except Exception as ex:
            self.log.error(f"Error al conectar a la pagina web: {ex}")
            return {
                "total_procesos": 0,
                "procesos": [],
            }

    #Funcion para consultar detalle de un proceso
    def consultar_detalleProceso(self,proceso):
        self.url = f"https://consultaprocesos.ramajudicial.gov.co:448/api/v2/Proceso/Detalle/{proceso}"
        try:
            response = requests.get(self.url,headers=self.headers)
            #Si la respuesta es exitosa, se devuelve el json
            if response.status_code == 200:
                self.log.info("Conexión exitosa a la página para detalle de un proceso")
                self.log.info(f"Detalle del proceso encontrado: {response.json()}")
                return response.json()
            #En caso de que no sea asi, se devuelve un mensaje de error
            else:
                self.log.warning(f"Error al conectar a la pagina web: {response.status_code}")
        except Exception as ex:
            self.log.error(f"Error al conectar a la pagina web: {ex}")

    #Funcion para consulrar de actuaciones de un proceso
    def consultar_actuacionesProcesoList(self,proceso):
        url = f"https://consultaprocesos.ramajudicial.gov.co:448/api/v2/Proceso/Actuaciones/{proceso}"
        try:
            response = requests.get(url, headers=self.headers)
            #Si la respuesta es exitosa, se devuelve el json
            if response.status_code == 200:
                self.log.info("Conexión exitosa a la página de consulta por número de radicado")

                #Una vez que tenfo la repsiesta llamo a la ia para pasarle los datos 
                ia = ConexionIA()
                #Llamo a la funcion de clasificar datos
                clasificacion = ia.clasificar_actuacionesList(response.json())

                #Limpio la respuesta de la IA
                utils = Utils()
                clasificacionJson = utils.limpiar_y_parsear_respuesta(clasificacion)

                self.log.info(f"Clasificacion de la IA: {(clasificacionJson)}")
                return clasificacionJson

            #En caso de que no sea asi, se devuelve un mensaje de error
            else:
                self.log.warning(f"Error al conectar a la pagina web: {response.status_code}")
        except Exception as ex:
            self.log.error(f"Error al conectar a la pagina web: {ex}")

    #FUncion para obtener la clase del proceso
    def obtener_tipoProceso(self,proceso):
        url = f"https://consultaprocesos.ramajudicial.gov.co:448/api/v2/Proceso/Detalle/{proceso}"
        try:
            response = requests.get(url, headers=self.headers)
            #Si la respuesta es exitosa, se devuelve el json
            if response.status_code == 200:
                data = response.json()
                #Extraigo el tipo de proceso
                tipo_proceso = data.get("tipoProceso","No disponible")
                #Extraigo la clase del proceso
                clase_proceso = data.get("claseProceso", "No disponible")

                return {
                    "tipo_proceso": tipo_proceso,
                    "clase_proceso": clase_proceso
                }

            #En caso de que no sea asi, se devuelve un mensaje de error
            else:
                self.log.warning(f"Error al conectar a la pagina web: {response.status_code}")
        except Exception as ex:
            self.log.error(f"Error al conectar a la pagina web: {ex}")
