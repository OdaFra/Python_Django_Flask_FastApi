from capa_datos.usuario_dao import UsuarioDAO
from loggers.logger import log
from capa_datos.usuario import Usuario

opcion=None

while opcion != 5:
    print('Opciones: ')
    print('1. Listar usuarios')
    print('2. Agregar usuarios')
    print('3. Modificar usuarios')
    print('4. Eliminar usuarios')
    print('5. Salir')
    opcion= int(input('Selecciona una opcion del 1 al 5: '))
    if opcion == 1:
        usuarios = UsuarioDAO.seleccionar()
        for usuario in usuarios:
            log.info(usuario)
    elif opcion == 2:
        user = input('Escribe el username: ')
        password = input('Escribe el password: ')
        usuario = Usuario(username=user, password=password)
        usuario_insertado = UsuarioDAO.insertar(usuario)
        log.info(f'Usuario insertado: {usuario_insertado}')
    elif opcion == 3:
        id_usuario = int(input('Escribe el id_usuario a modificar: '))
        username = input('Escribe el username: ')
        password = input('Escribe el password: ')
        usuario = Usuario(id_usuario, username, password)
        usuario_actualizado = UsuarioDAO.actualizar(usuario)
        log.info(f'Usuario actualizado: {usuario_actualizado}')
    elif opcion == 4:
        id_usuario = int(input('Escribe el id_usuario a eliminar: '))
        usuario  = Usuario(id_user=id_usuario)
        usuario_eliminado = UsuarioDAO.eliminar(usuario)
        log.info(f'Usuario eliminado: {usuario_eliminado}')
else:
    log.info('El programa ha terminado...')