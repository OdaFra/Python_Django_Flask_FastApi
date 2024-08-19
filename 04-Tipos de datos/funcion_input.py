#Funcion input para procesar la entrada del usuario.

# resultado = input('Por favor ingresa un mensaje:')
# print('El valor proporcionado es: ', resultado)
# print('Fin proceso')

#Conversion  de str a int para proceso sencillo de suma.

# x = int(input('Escribe el primer numero: '))
# y = int(input('Escribe el segundo numero: '))
# res = x+y
# print('El resultado es: ', res)

#Ejericio 1
# data = int(input('Como estuvo tu dia: '))
# print('Mi dia estuvo: ', data)

#Ejercicio 2
# print('INFORMACION NECESARIA')
# titulo = input('Proporciona un titulo: ')
# autor = input('Proporciona un autor: ')
# print(titulo, ' fue escrito por el ', autor)

#Ejericio 3 - Sistema de generador de ID unico

from random import randint

nombre=input('Introduce tu Nombre: ')
apellido=input('Introduce tu Apellido: ')
anho=input('Introduce tu fecha de nacimiento: ')
rango = randint(0,9999)
id_unico = nombre.strip().upper()[0:2]+apellido.strip().upper()[0:2]+anho.strip()[2:]+rango[3:]
print(f'El ID es: {id_unico}')



