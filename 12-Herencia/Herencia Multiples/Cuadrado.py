from FiguraGeometrica import FiguraGeometrica
from Color import Color

class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, alto, ancho, color):
        # super().__init__(lado, color)
        FiguraGeometrica.__init__(self, alto, ancho)
        Color.__init__(self, color)
    
    def calcular_area(self):
        return self.alto * self.ancho