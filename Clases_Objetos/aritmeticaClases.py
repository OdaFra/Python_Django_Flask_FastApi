class Aritmetica:
    """
    Clase aritmeticas para realizar las operaciones sumar, restar, multiplicar, etc.
    """

    # Self es una referencia a si mismo al momento de crear un objeto de esta clase
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def sumar(self):
        return self.x + self.y
    def restar(self):
        return self.x - self.y
    def multiplicar(self):
        return self.x * self.y
    def division(self):
        return self.x / self.y

result = Aritmetica(99,25)
print(f'La suma es: {result.sumar()}')
print(f'La resta es: {result.restar()}')
print(f'La multiplicacion es: {result.multiplicar()}')
print(f'La division es: {result.division():.2F}')
