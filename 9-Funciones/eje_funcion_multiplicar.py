'''
Crear una funcion para sumar los valores recibidos de tipo numerico, utilizando argumentos variables *args
como parametro de la funcion y regresar como resultado la suma de todos los valores pasados por argumentos.
'''

def multiplicarValores(*args):
    res=1
    for valor in args:
        res*=valor
    return res

print(multiplicarValores(10,20,10))