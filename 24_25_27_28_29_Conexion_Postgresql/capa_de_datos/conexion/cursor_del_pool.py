import sys
import os 

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from  capa_de_datos.conexion.conexion import Conexion
from capa_de_datos.loggers.logger import log 

class CursorDelPool:
    def __init__(self):
        self._conexion = None
        self._cursor = None
    
    def __enter__(self):
        log.debug('Inicio del metodo with __enter__')
        self._conexion = Conexion.obtenerConexion()
        self._cursor = self._conexion.cursor()
        return self._cursor

    def __exit__(self, tipo_excepcion, valor_excepcion, traceback_excepcion):
        log.debug('Se ejecuta metodo __exit__')
        if valor_excepcion:
            self._conexion.rollback()
            log.error(f'Ocurrio una excepcion, se aplica rollback: {valor_excepcion}, {tipo_excepcion}, {traceback_excepcion}')
        else:
            self._conexion.commit()
            log.debug('Commint de la transaccion')
        self._cursor.close()
        Conexion.liberarConexion(self._conexion)

if __name__ == '__main__':
    with CursorDelPool() as cursor:
        log.debug('Dentro del bloque With')
        cursor.execute('Select * From "Persona" order by id_persona')
        print(log.debug(cursor.fetchall()))
        