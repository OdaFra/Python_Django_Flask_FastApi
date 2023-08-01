class Cubo:
    def __init__(self, ancho, altura, profundidad):
        self.ancho = ancho
        self.altura = altura
        self.profundidad = profundidad

    def calcularVolumen(self):
        volumen = self.ancho * self.altura * self.profundidad
        return volumen


ancho = float(input("Proporcione la ancho: "))
altura = float(input("Proporcione la altura: "))
profundidad = float(input("Proporcione la profundidad: "))

result = Cubo(ancho, altura, profundidad)
print(f"El area del rectangulo es: {result.calcularVolumen()}")
