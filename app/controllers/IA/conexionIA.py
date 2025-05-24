import openai
import json

from app.models.logger import Logger


#Clase para manejar la conexion con la IA
class ConexionIA:
    def __init__(self):
        self.api_key = "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"
        self.model = "gpt-3.5-turbo"
        self.log = Logger("logs/ConexionIA.log").get_logger()
        self.openai = openai.api_key = self.api_key
    

    #Funcion para recibir los datos y clasificarlos
    def clasificar_datos(self, datos):
        try:
            prompt = """
                Eres un asistente jurídico. A continuación tienes una lista de eventos judiciales (actuaciones). Para cada actuación, clasifícala según su nivel de urgencia para el abogado defensor y proporciona un resumen breve.

                Clasificación: Alta, Media, Baja o Nula.

                Devuelve la información en este formato y las de mayor urgencia primero, y en un formato json con estas estructuras:

                [
                    {
                        "actuacion": <número>,
                        "clasificacion": "Alta" | "Media" | "Baja" | "Nula",
                        "resumen": "<texto resumen>"
                    },
                    ...
                ]

                Lista de actuaciones:
            """

            datos_str = json.dumps(datos, ensure_ascii=False)

            response = openai.chat.completions.create(
                model="gpt-4o",  # También puedes usar gpt-4-turbo o gpt-3.5-turbo
                messages=[
                    {"role": "system", "content": prompt},
                    {"role": "user", "content": f"Clasifica el siguiente evento judicial: {datos_str}"}
                ],
                temperature=0.3
            )

            return response.choices[0].message.content.strip()
        except Exception as ex:
            self.log.error(f"Error al clasificar los datos: {ex}")
            return None
