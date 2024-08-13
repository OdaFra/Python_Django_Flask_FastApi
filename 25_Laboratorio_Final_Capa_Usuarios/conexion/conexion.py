# import psycopg2 as db
import sys
import os
from  psycopg2 import pool

# Para poder ubicar la ruta del archivo a importar
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from loggers.logger import log 

class Conexion:
    _DATABASE = "postgres"
    _USERNAME = "postgres"
    _PASSWORD = "123456"
    _DB_PORT = "5432"
    _HOST = "localhost"
    _MIN_CON = 2
    _MAX_CON = 5
    _pool = None
    # _conexion = None
    # _cursor = None

    #Para obtener una Pool de conexiones..!
    @classmethod
    def obtenerPool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(
                    cls._MIN_CON,
                    cls._MAX_CON,
                    host=cls._HOST,
                    port=cls._DB_PORT,
                    user=cls._USERNAME,
                    password=cls._PASSWORD,
                    database=cls._DATABASE,
                )
                log.debug(f'Conexion exitosa: {cls._pool}')
                return cls._pool
            except Exception as e:
                print(f"Ocurrio un error al obtener el pool de conexiones")
                sys.exit()
        else:
            return cls._pool

    @classmethod
    def obtenerConexion(cls):
        #Obtener un solo objeto de conexion a la base de datos!
        conexion = cls.obtenerPool().getconn()
        log.debug(f'Conexion exitosa al obtener un pool de conexion: {conexion}')
        return conexion
    
        # if cls._conexion is None:
        #     try:
        #         cls._conexion = db.connect(
        #             host=cls._HOST,
        #             port=cls._DB_PORT,
        #             user=cls._USERNAME,
        #             password=cls._PASSWORD,
        #             database=cls._DATABASE,
        #         )
        #         log.debug(f'Conexion exitosa: {cls._conexion}')
        #         return cls._conexion

        #     except Exception as e:
        #         log.error(f"Ocurrio un error al tratar de obtener la conexion:{e}")
        #         sys.exit()
        # else:
        #     return cls._conexion
    
    #Liberar conexion
    @classmethod
    def liberarConexion(cls, conexion):
        cls.obtenerPool().putconn(conexion)
        log.debug(f'Regresamos la conexion al pool de conexiones {conexion}!!')
    
    #Cerrar por completo la conexion
    @classmethod
    def cerrarConexion(cls):
        cls.obtenerPool().closeall()
            
        
        
        

    # @classmethod
    # def obtenerCursor(cls):
    #     if cls._cursor is None:
    #         try:
    #             cls._cursor = cls.obtenerConexion().cursor()
    #             logger.debug(f"Conexion exitosa [cursor] : {cls._cursor}")
    #             return cls._cursor
    #         except Exception as e:
    #             logger.error(f"Ocurrio un error al tratar de obtener el cursor:{e}")
    #             sys.exit()
    #     else:
    #         return cls._cursor


# testing
if __name__ == "__main__":
    pool1 = Conexion.obtenerConexion()
    Conexion.liberarConexion(pool1)
    pool2 = Conexion.obtenerConexion()
    
    
