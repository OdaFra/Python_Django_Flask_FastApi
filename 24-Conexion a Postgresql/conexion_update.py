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
            #Creamos la sentencia para actualizar
            # sentencia = 'UPDATE "Persona" set nombre=%s, apellido=%s, email=%s Where id_persona=%s'
            # valores = ('Alberto', 'Franco', 'afranco@test.com',6)
            
            #Actualizar varios registro
            sentencia = 'UPDATE "Persona" set email=%s Where id_persona=%s'
            valores = (('test@test.com',4),('test1@test.com',5))
            cursor.executemany(sentencia,valores)
            registro_actualizado = cursor.rowcount
            print(f'Registros insertados: {registro_actualizado}')
except Exception as e:
    print (f'Ocurrio un error:{e}')
finally:
    #cursor.close()
    conexion.close()
