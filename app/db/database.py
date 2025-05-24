import mysql.connector
from mysql.connector import Error
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from app.models.logger import Logger

#Clase para mnejar la base de datos postgres
class ConexionDB:

    #Constructor
    def __init__(self):
        self.log = Logger("logs/Conexion.log").get_logger()
        self.host = "localhost"
        self.port = 3306
        self.user = "root"
        self.password = "root"
        self.database = "BotTech"
    
    #Metodo para conectar a la base de datos
    def conectar(self):
        try:
            con = mysql.connector.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
            )
            if con.is_connected():
                self.log.info("Conexión exitosa a la base de datos")
                return con
            else:
                self.log.error("Error al conectar a la base de datos")
                return None
        except Error as ex:
            self.log.error(f"Error al conectar a la base de datos: {ex}")
    
    #Funcion para desconectar la base de datos
    def desconectar(self, con):
        try:
            if con.is_connected():
                con.close()
                self.log.info("Desconexión exitosa de la base de datos")
            else:
                self.log.error("Error al desconectar de la base de datos")
        except Error as ex:
            self.log.error(f"Error al desconectar de la base de datos: {ex}")