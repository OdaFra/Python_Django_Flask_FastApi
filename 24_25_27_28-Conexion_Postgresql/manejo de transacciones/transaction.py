import psycopg2 as pgdb

conexion = pgdb.connect(
    user = 'postgres',
    password = '123456',
    host = 'localhost',
    port = '5432',
    database = 'postgres'
)
#Example for transaction
try:
    #Autocommit in false
    conexion.autocommit = False
    cursor = conexion.cursor()
    #Insert
    # sentencia = 'INSERT INTO "Persona"(nombre, apellido, email) values (%s,%s,%s)'        
    # valores = ('Pedro', 'Coronel','pc@test.com')
    # cursor.execute(sentencia, valores)
    #Update
    sentencia = 'Update "Persona" set nombre=%s, apellido=%s, email=%s where id_persona=%s'        
    valores = ('Montse', 'Iglesias','mi@test.com', 8)
    cursor.execute(sentencia, valores)
    #set commit at the end
    conexion.commit()
    print('Termina la transaccion...!')
except Exception as e:
    conexion.rollback()
    print (f'Ocurrio un error:{e}, se genera rollback..')
finally:
    #cursor.close()
    conexion.close()
