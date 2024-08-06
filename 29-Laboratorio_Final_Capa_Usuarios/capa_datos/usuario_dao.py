import sys
import os


# Para poder ubicar la ruta del archivo a importar
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

from conexion.cursor_del_pool import CursordelPool
from capa_datos.usuario import Usuario
from loggers.logger import log


class UsuarioDAO:
    """
    DAO - Data access Object para la tabla de usuario
    CRUD
    """

    _SELECCIONAR = 'Select * From "Usuario" order by id_user'
    _INSERTAR = 'INSERT INTO "Usuario" (username, password) values (%s,%s)'
    _ACTUALIZAR = 'UPDATE "Usuario" set username=%s, password=%s Where id_user=%s'
    _ELIMINAR = 'DELETE FROM "Usuario" WHERE id_user = %s'

    @classmethod
    def seleccionar(cls):
        #    with Conexion.obtenerConexion()as conexion:
        with CursordelPool() as cursor:
            log.debug("Seleccionamos usuarios")
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            usuarios = []
            for registro in registros:
                usuario = Usuario(
                    registro[0],
                    registro[1],
                    registro[2],
                )
                usuarios.append(usuario)
        return usuarios

    @classmethod
    def insertar(cls, usuario):
        # with Conexion.obtenerConexion():
        with CursordelPool() as cursor:
            log.debug(f"Usuario a insertar: {usuario}")
            valores = (usuario.username, usuario.password)
            cursor.execute(cls._INSERTAR, valores)
        return cursor.rowcount

    @classmethod
    def actualizar(cls, usuario):
        #  with Conexion.obtenerConexion():
        with CursordelPool() as cursor:
            log.debug(f"Usuario a actualizar: {usuario}")
            valores = (usuario.username, usuario.password, usuario.id_user)
            cursor.execute(cls._ACTUALIZAR, valores)
        return cursor.rowcount

    @classmethod
    def eliminar(cls, usuario):
        #  with Conexion.obtenerConexion():
        with CursordelPool() as cursor:
            log.debug(f"Usuario a eliminar: {usuario}")
            valores = (usuario.id_user,)
            cursor.execute(cls._ELIMINAR, valores)
        return cursor.rowcount


if __name__ == "__main__":
    # #Insert
    # usuario = Usuario(username="goz", password="1234")
    # usuario_insertado = UsuarioDAO.insertar(usuario)
    # log.debug(f"Usuario Insertado: {usuario_insertado}")

    # Update
    usuario = Usuario(3,'goz', '12345')
    usuario_actualizado = UsuarioDAO .actualizar(usuario)
    log.debug(f'Usuario actualizado: {usuario_actualizado}')

    # Delete
    # persona = Persona(id_persona=13)
    # persona_eliminada = PersonaDAO.eliminar(persona)
    # logger.debug(f'Persona eliminada: {persona_eliminada}')

    # Select
    usuarios = UsuarioDAO.seleccionar()
    for usuario in usuarios:
        log.debug(usuario)
