import psycopg2 as pgdb

conexion = pgdb.connect(
    user = 'postgres',
    password = '123456',
    host = 'localhost',
    port = '5432',
    database = 'postgres'
)

# print(conexion)
with conexion:
    #creamos el cursor hacia la db
    with conexion.cursor() as cursor:
        #generamos la sentencia a utilizar
        sentencia = 'Select nombre, apellido FROM "Persona"'
        #ejectuamos la sentencia por medio del cursor
        cursor.execute(sentencia)
        #obtenemos toda la informacion de la sentencia ejecutada en un lista (con tuplas)
        res = cursor.fetchall()

print(res)

cursor.close()
conexion.close()
