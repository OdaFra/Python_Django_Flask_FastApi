#SET
planetas = {'marte', 'jupiter', 'venus'}

print(planetas)

#Largo del elemento
print(len(planetas))

#Revisar si un elemento esta presente
print('martes' in planetas)

#Agregar un nuevo elemento 
planetas.add('tierra')
print(planetas)

#Eliminar un elemento arrojando un error en caso de que no la ubique
planetas.remove('tierra')
print(planetas)

#Tambien para eliminar un elemento sin arrojar un error
planetas.discard('tierra')
print(planetas)

#limpiar el set
planetas.clear()
print(planetas)
