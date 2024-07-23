import psycopg2 as pgdb

conexion = pgdb.connect(
    user = 'postgres',
    password = '123456',
    host = 'localhost',
    port = '5432',
    database = 'postgres'
)
#Example for transaction (With)
try:
    with conexion:
        with conexion.cursor() as cursor:
        #Update
            sentencia = 'Update "Persona" set  email=%s where id_persona=%s'        #nombre=%s, apellido=%s,
            valores = ('miglesias@test.com', 8)
            cursor.execute(sentencia, valores)
            #set commit at the end
            print('Termina la transaccion...!')
except Exception as e:
    print (f'Ocurrio un error:{e}, se genera rollback..')
finally:
    cursor.close()
    print('Se ha finalizado proceso en la DB..!')    
