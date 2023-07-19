'''
Crear una funcion para sumar los valores recibidos de tipo numerico, utilizando argumentos variables *args
como parametro de la funcion y regresar como resultado la suma de todos los valores pasados por argumentos.
'''

def sumaValores(*args):
    res=0
    for valor in args:
        res +=valor
    return res

print(sumaValores(10, 10,40, 50))
        