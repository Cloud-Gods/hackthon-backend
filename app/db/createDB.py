import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from app.models.logger import Logger
from app.db.database import ConexionDB

#Clase para crear la base de datos
class CreateDB:
    def __init__(self):
        self.log = Logger("logs/Conexion.log").get_logger()
        self.con = ConexionDB().conectar()


    #Funcion para crear la base de datos
    def crear_base_datos(self):
        try:
            cursor = self.con.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS BotTech")
            self.log.info("Base de datos creada exitosamente")
            self.crear_tablas()
        except Exception as ex:
            self.log.error(f"Error al crear la base de datos: {ex}")
        finally:
            cursor.close()
    
    #Funcion para crear las tablas
    def crear_tablas(self):
        try:
            cursor = self.con.cursor()
            # Crear tabla de usuarios
            cursor.execute("""
                Use  BotTech;
                CREATE TABLE IF NOT EXISTS Documentos (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nombre VARCHAR(255) NOT NULL,
                    tipo VARCHAR(50) NOT NULL,
                    fecha DATE NOT NULL
                )
            """)
            self.log.info("Tabla de usuarios creada exitosamente")
        except Exception as ex:
            self.log.error(f"Error al crear la tabla de Documentos: {ex}")
        finally:
            cursor.close()