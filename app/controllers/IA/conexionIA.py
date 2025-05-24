import openai
import json
from app.core.secretManager import SecretManager
from app.models.logger import Logger


#Clase para manejar la conexion con la IA
class ConexionIA:
    def __init__(self):
        self.api_key = SecretManager().get_secret()
        self.log = Logger("logs/ConexionIA.log").get_logger()
        self.openai = openai.api_key = self.api_key

    #Funcion para recibir los datos y clasificarlos
    def clasificar_actuacionesList(self, datos):
        try:
            prompt = """
                Eres un asistente jurídico. A continuación tienes una lista de eventos judiciales (actuaciones). Para cada actuación, clasifícala según su nivel de urgencia para el abogado defensor y proporciona un resumen breve.

                Clasificación: Alta, Media, Baja o Nula.

                Alta: Actuaciones que requieren atención inmediata o que tienen un impacto significativo en el caso.
                Media: Actuaciones que son importantes pero no urgentes.
                Baja: Actuaciones que son de bajo impacto o que pueden esperar.
                Nula: Actuaciones que no tienen relevancia o que no requieren atención.

                LAs actuaciones las vas a colocar con numoer siendo 1 la de menor urgencia y 4 la de mayor urgencia.

                Pero en caso de que no haya actuaciones, devuelve un mensaje indicando que no hay actuaciones.

                Devuelve la información en este formato y las de mayor urgencia primero, y en un formato json con estas estructuras:

                [
                    {
                        "actuacion": <número>,
                        "clasificacion": "Alta"= 4 | "Media" = 3 | "Baja" = 2 | "Nula" = 1,
                        "resumen": "<texto resumen>"
                    },
                    ...
                ]

                Lista de actuaciones:
            """

            datos_str = json.dumps(datos, ensure_ascii=False)

            response = openai.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": prompt},
                    {"role": "user", "content": f"Clasifica el siguiente evento judicial: {datos_str}"}
                ],
                temperature=0.3

            )

            return response.choices[0].message.content.strip()
        except Exception as ex:
            self.log.error(f"Error al clasificar los datos: {ex}")
            return {
                "error": "Error al clasificar los datos"
            }
    
    #Funcion para mirar por encima que trata el proceso