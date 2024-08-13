# Bool contine los valores true y false

# Tipos numericos son representados por False = 0 y los demas valores son True
valor = 0
res = bool(valor)
print(f'El valor es: {valor}, y su resultado es: {res}')
valor = 15
res = bool(valor)
print(f'El valor es: {valor}, y su resultado es: {res}')

#Para el tipo STR, False '' y si contiene valor es True
valor = ''
res = bool(valor)
print(f'El valor en str es: {valor}, y su resultado es: {res}')
valor = 'Hey Coders'
res = bool(valor)
print(f'El valor en str es: {valor}, y su resultado es: {res}')


#Para el tipo de colecciones o listas, False [] y si contiene valor es True
valor = []
res = bool(valor)
print(f'El valor en lista es: {valor}, y su resultado es: {res}')
valor = ['Hey','Coders']
res = bool(valor)
print(f'El valor en lista es: {valor}, y su resultado es: {res}')

#Para el tipo de datos tupla , False () y si contiene valor es True
valor = ()
res = bool(valor)
print(f'El valor en tupla es: {valor}, y su resultado es: {res}')
valor = (1,2,3)
res = bool(valor)
print(f'El valor en tupla es: {valor}, y su resultado es: {res}')

#Para el tipo de datos diccionario , False {} y si contiene valor es True
valor = {}
res = bool(valor)
print(f'El valor en tupla es: {valor}, y su resultado es: {res}')
valor = {'nombre':'Juan'}
res = bool(valor)
print(f'El valor en tupla es: {valor}, y su resultado es: {res}')


#Control de sentencias
valor = ''

if valor:
    print('Verdadero')
else:
    print('Falso')

