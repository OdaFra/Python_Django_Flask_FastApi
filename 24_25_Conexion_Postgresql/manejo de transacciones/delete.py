import psycopg2 as pgdb

conexion = pgdb.connect(
    user = 'postgres',
    password = '123456',
    host = 'localhost',
    port = '5432',
    database = 'postgres'
)

try:
# print(conexion)
    with conexion:
        #creamos el cursor hacia la db
        with conexion.cursor() as cursor:
            #Creamos la sentencia delete
            sentencia = 'DELETE FROM "Persona" where id_persona in %s'
            #Entrada del input
            entrada = input('Por favor proporcione los valores separados por coma: ')
            #El valor del id_persona a eliminar    
            valores = (tuple(entrada.split(',')),)
            cursor.execute(sentencia, valores)
            registros_eliminados = cursor.rowcount
            print(f'Registros eliminados: {registros_eliminados}')
except Exception as e:
    print (f'Ocurrio un error:{e}')
finally:
    #cursor.close()
    conexion.close()
