import sys
import os
#Para poder ubicar la ruta del archivo a importar
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../capa_de_datos')))

from conexion.cursor_del_pool import CursorDelPool
from persona import Persona
from  conexion.conexion import Conexion
from  capa_de_datos.loggers.logger import log



class PersonaDAO:
    '''
    DAO (Data Acess Object) \n
    CRUD (Create - Read - Update - Delete)
    '''
    _SELECCIONAR = 'Select * From "Persona" order by id_persona'
    _INSERTAR = 'INSERT INTO "Persona"(nombre, apellido, email) values (%s,%s,%s)'
    _ACTUALIZAR = 'UPDATE "Persona" set nombre=%s, apellido=%s, email=%s Where id_persona=%s'
    _ELIMINAR = 'DELETE FROM "Persona" WHERE id_persona = %s'
    
    @classmethod
    def seleccionar(cls):
    #    with Conexion.obtenerConexion()as conexion:
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            personas = [];
            for registro in registros:
                persona = Persona(registro[0],registro[1], registro[2], registro[3],)
                personas.append(persona)
        return personas
        
    @classmethod
    def insertar(cls, persona):
        # with Conexion.obtenerConexion():
            with CursorDelPool() as cursor:
                valores = (persona.nombre, persona.apellido, persona.email)
                cursor.execute(cls._INSERTAR, valores)
                log.debug(f'Persona a insertar: {persona}')
            return cursor.rowcount
    
    @classmethod
    def actualizar(cls, persona):
        #  with Conexion.obtenerConexion():
            with CursorDelPool() as cursor:
                valores = (persona.nombre, persona.apellido, persona.email,persona.id_persona)
                cursor.execute(cls._ACTUALIZAR, valores)
                log.debug(f'Persona actualizada: {persona}')
            return cursor.rowcount
            
    @classmethod
    def eliminar(cls, persona):
        #  with Conexion.obtenerConexion():
            with CursorDelPool() as cursor:
                valores = (persona.id_persona,)
                cursor.execute(cls._ELIMINAR, valores)
                log.debug(f'Persona eliminada: {persona}')
            return cursor.rowcount


if __name__ == '__main__':
    # #Insert
    # persona = Persona(nombre='Noha', apellido='Ramirez', email='nr@test.com')
    # personas_insertadas =PersonaDAO.insertar(persona)
    # log.debug(f'personas insertadas: {personas_insertadas}')
    
    #Update
    persona = Persona(10,'Fernando', 'Herrera', 'fh@test.com')
    personas_actualizadas = PersonaDAO.actualizar(persona)
    log.debug(f'Personas actualizadas: {personas_actualizadas}')
    
    #Delete
    # persona = Persona(id_persona=13)
    # persona_eliminada = PersonaDAO.eliminar(persona)
    # log.debug(f'Persona eliminada: {persona_eliminada}')
    
    
    #Select
    personas = PersonaDAO.seleccionar()
    for persona in personas:
        log.debug(persona)