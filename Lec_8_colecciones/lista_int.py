nombres = ['oscar','david','ramirez','franco']

#Imprime la lista tal cual como recibe
print(nombres)

#Imprimir por la ultima ubicacion 
print(nombres[-1])

#Imprimir por rango.
print(nombres[0:2])

#Ir desde el inicio de la lista al indice (sin incluirlo)
print(nombres[:3])

#Desde el indice indicado hasta el final
print(nombres[1:])

#Cambiar un valor de la lista
nombres[2]='juan'
print(nombres)

#Iterar los elementos de la lista.

for name in nombres:
    print(name)
else:
    print('No existe mas nombre en la lista')    


#Confirmar cantidad de elementos de una lista
print(len(nombres))

#Agregar un nuevo elemento a lista
nombres.append('alberto')
print(nombres)

#Insertar un elemento a un indice especifico.
nombres.insert(1, 'justo')
print(nombres)

#Remover un valor de la lista
nombres.remove('justo')
print(nombres)

#Remover el ultimo elemento de la lista
nombres.pop()
print(nombres)

#Eliminar un indice de la lista
del nombres[0]
print(nombres)

#Eliminar todos los elementos de la lista
nombres.clear()
print(nombres)