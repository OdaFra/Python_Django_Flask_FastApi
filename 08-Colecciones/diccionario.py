#Dict (key, value)
diccionario={
    'IDE':'Integrated Development Environment',
    'OOP':'Object Oriented Programming',
    'DBMS':'Database Management System'
}

print(diccionario)
print(len(diccionario))

#Para acceder  aun elemento de un diccionario
# 1-
print(diccionario['OOP'])

# 2-
print(diccionario.get('IDE'))

# Modificando un elemento
diccionario['DBMS']='Database MANAGEMENT SyStem Linux'
print(diccionario)

#Recorrer elementos de un diccionario.
for termino, valor in diccionario.items():
    print(termino,valor)


for termino in diccionario.keys():
    print(f'Las llaves son: {termino}')

for valor in diccionario.values():
    print(f'Los valores son: {valor}')
    
#comprobar la existencia de un elemento
print('IDE' in diccionario)

#Agregar un elemento al diccionario
diccionario['PK']='Primary key'

print(diccionario)

#remover un elemento del diccionario
diccionario.pop('DBMS')
print(f'{diccionario}')

#Eliminar 
diccionario.clear()
print(diccionario)