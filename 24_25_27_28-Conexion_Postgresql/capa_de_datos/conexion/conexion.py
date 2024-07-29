import psycopg2 as db
import sys
import os
#Para poder ubicar la ruta del archivo a importar
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from  capa_de_datos.loggers.logger import log

class Conexion:
    _DATABASE = "postgres"
    _USERNAME = "postgres"
    _PASSWORD = "123456"
    _DB_PORT = "5432"
    _HOST = "localhost"
    _conexion = None
    _cursor = None

    @classmethod
    def getConexion(cls):
        if cls._conexion is None:
            try:
                cls._conexion = db.connect(
                    host=cls._HOST,
                    port=cls._DB_PORT,
                    user=cls._USERNAME,
                    password=cls._PASSWORD,
                    database=cls._DATABASE,
                )
                log.debug(f'Conexion exitosa: {cls._conexion}')
                return cls._conexion
            
            except Exception as e:
                log.error(f"Ocurrio un error al tratar de obtener la conexion:{e}")
                sys.exit()
        else:
            return cls._conexion
    
    @classmethod
    def getCursor(cls):
        if cls._cursor is None:
           try:
             cls._cursor = cls.getConexion().cursor()
             log.debug(f'Conexion exitosa [cursor] : {cls._cursor}')
             return cls._cursor
           except Exception as e:
             log.error(f"Ocurrio un error al tratar de obtener el cursor:{e}")
             sys.exit()
        else:
            return cls._cursor

#testing
if __name__ == '__main__':
    Conexion.getConexion()
    Conexion.getCursor()