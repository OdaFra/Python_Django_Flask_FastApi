class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcularArea(self):
        area = self.base * self.altura
        return area


base = float(input("Proporcione la base: "))
altura = float(input("Proporcione la altura: "))

result = Rectangulo(base, altura)
print(f"El area del rectangulo es: {result.calcularArea()}")
