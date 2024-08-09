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
            #generamos la sentencia a utilizar y obtener todas los registros
            #sentencia = 'Select * FROM "Persona"'
            #para obtener solo un registro
            sentencia = 'Select * From "Persona" where id_persona in %s'
            #id_persona= input('Proporcione el valor de id_persona: ')#2
            # ids = ((1,3),)
            entradas = input('Proporciona los ids a buscar separados por comas: ')
            ids = (tuple(entradas.split(',')),)
            #ejectuamos la sentencia por medio del cursor
            cursor.execute(sentencia, ids)
            #obtenemos toda la informacion de la sentencia ejecutada en un lista (con tuplas)
            #res = cursor.fetchall()
            #obtener solo un registro
            res = cursor.fetchall()
            
            print(res)
except Exception as e:
    print (f'Ocurrio un error:{e}')
finally:
    #cursor.close()
    conexion.close()
