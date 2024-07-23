#Iterar un rango de 0 a 10 e imprimit numeros divisible entre 3
for i in range(11):
   if i % 3 == 0:
       print(i)
else:
    print('Ya no se dispone de nros en la lista')

#Crear un rango de numeros de 2 a 6, e imprimelos
for i in range(2,7):
    #if i % 2 == 0:
       # if i >=2 or i <=6:
    print(i)
else:
    print('Ya no se dispone de nros en la lista')

#Crear un rango de 3 a 10 pero con incremento de 2 en 2.

rango = range(3,11,2)
for i in rango:
    print(i)
else:
    print('Ya no se dispone de nros en la lista')