#definir una tupla
frutas=('manzana','pera','banana', 'naranja')
print(frutas)

#Acceder a una posicion de la tupla
print(frutas[1])

#Acceder al ultimo valor de la tupla
print(frutas[-1])

#Acceder por rango a los valores de la tupla
print(frutas[1:3])

#Recorrer o iterar elementos

for fruta in frutas:
    print(fruta, end=' ')
    