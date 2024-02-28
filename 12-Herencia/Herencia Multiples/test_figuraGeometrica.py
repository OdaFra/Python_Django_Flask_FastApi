from Cuadrado import Cuadrado

cuadrado1 = Cuadrado(10,20,'azul')
print(cuadrado1.alto)
print(cuadrado1.ancho)
print(cuadrado1.color)
print(cuadrado1.calcular_area())

#METODO MRO Method Resolution Order - Permiter conocer el orden en llamada a las clases heredadas

print(Cuadrado.mro())