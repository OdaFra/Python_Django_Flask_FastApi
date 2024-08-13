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
            #Creamos la sentencia Insert
            sentencia = 'INSERT INTO "Persona"(nombre, apellido, email) values (%s,%s,%s)'
            #Para insertar solo una registro
            # valores = ('Montse', 'Iglesias','miglesias@test.com')
            #Para insertar varios registros
            valores = (('David', 'Ramirez','dramirez@test.com'),('Oscar', 'Ramirez','oramirez@test.com'))
            cursor.executemany(sentencia, valores)
            #Aplicar commit()
            #Aplicar registro insertados
            registro_insertados = cursor.rowcount
            print(f'Registros insertados: {registro_insertados}')
except Exception as e:
    print (f'Ocurrio un error:{e}')
finally:
    #cursor.close()
    conexion.close()
