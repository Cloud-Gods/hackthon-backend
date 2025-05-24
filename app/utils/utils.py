import json
import re
from app.models.logger import Logger

#Clase para manejar funciones varias que se pueden retulizar en un futuro
class Utils:
    def __init__(self):
        self.log = Logger("logs/Utils.log").get_logger()
    
    def limpiar_y_parsear_respuesta(self,respuesta_ia: str):
        try:
            # Elimina las etiquetas ```json y ``` si existen
            respuesta_limpia = re.sub(r"```json|```", "", respuesta_ia).strip()

            # Convierte a JSON
            datos_json = json.loads(respuesta_limpia)
            return datos_json
        except json.JSONDecodeError as ex:
            self.log.info("Error al convertir a JSON:", ex)
            return None
