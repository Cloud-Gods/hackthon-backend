import boto3
from botocore.exceptions import ClientError
import sys
import json
sys.path.append("c:/Users/yeiso/OneDrive/Escritorio/Proyecto/TalentoTech/Hackathon/hackthon-backend")
from app.models.logger import Logger


#Clase para manejar los secretos de AWS
class SecretManager:

    def __init__(self):

        self.secret_name = "Hackathon/Tech/Api-IA"
        self.region_name = "us-east-1"
        self.log = Logger("logs/SecretManager.log").get_logger()

    def get_secret(self):

        # Create a Secrets Manager client
        session = boto3.session.Session()
        client = session.client(
            service_name='secretsmanager',
            region_name=self.region_name
        )

        try:
            get_secret_value_response = client.get_secret_value(
                SecretId=self.secret_name
            )
        except ClientError as ex:
            self.log.error(f"Error al obtener el secreto: {ex}")

        secret = json.loads(get_secret_value_response['SecretString'])
        token= secret["api-TechBot"]
        return token