class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
    
    def __str__(self):
        return f'El vehiculo tiene el color: {self.color}, ruedas: {self.ruedas}'

class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        
    def __str__(self):
        return f'{super().__str__()}, la velocidad es: {self.velocidad}'

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo= tipo
    
    def __str__(self):
        return f'{super().__str__()}, el tipo es: {self.tipo}'
    

vehiculo = Vehiculo('Azul', '4')
coche = Coche('Rojo', 4,'120km')
bicicleta = Bicicleta('Verde', 2, 'Carrera')
print(vehiculo)
print(coche)
print(bicicleta)
