from Cuadrado import Cuadrado
from Rectangulo import Rectangulo

from FiguraGeometrica import FiguraGeometrica

#No se puede instanciar una clase abstracta
#figuraGeo = FiguraGeometrica()


print("Creacion de objeto cuadrado".center(50, "-"))
cuadrado1 = Cuadrado(5, 20, "azul")
cuadrado1.ancho = 12
areaCuadrado = cuadrado1.calcular_area()

# METODO MRO Method Resolution Order - Permiter conocer el orden en llamada a las clases heredadas

#Se modifica el metodo resolucion order.
print(Cuadrado.mro())
print(f"{cuadrado1}, su area es: {areaCuadrado}")

# Rectangulo

print("Creacion de objeto Rectangulo".center(50, "-"))
rectangulo = Rectangulo(5, 8, "Amarillo")
rectangulo.alto = 15
areaRectangulo = rectangulo.calcular_area()
print(f"{rectangulo}, su area es: {areaRectangulo}")
