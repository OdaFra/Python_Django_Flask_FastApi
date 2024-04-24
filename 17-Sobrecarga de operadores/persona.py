#Sobrecarga de operador segun metodo
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def __add__(self, valor):
        return f'{self.nombre} {valor.nombre}'
    
    def __sub__(self, value):
        return  f'{self.edad - value.edad}'
    
persona1 = Persona('Juan ', 2024)
persona2= Persona('Alberto', 1993)
print(persona1 + persona2 ) 
print(persona1 - persona2 ) 