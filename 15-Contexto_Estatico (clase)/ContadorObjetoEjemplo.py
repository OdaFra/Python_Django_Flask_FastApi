class Persona:
    contador_personas = 0

    #mejorar el contador con un metodo de clase
    @classmethod
    def generar_siguiente_valor(cls):
        cls.contador_personas+=1
        return cls.contador_personas
    
    def __init__(self, nombre, edad):
        self.id_persona = Persona.generar_siguiente_valor()
        self.nombre = nombre
        self.edad = edad
    
    def __str__(self):
            return f'Persona [{self.id_persona}, {self.nombre}, {self.edad} ]'


Persona1 = Persona('Juan', 12)
Persona2 = Persona('Alberto', 30)
Persona3 = Persona('Naho', 7)

print(Persona1)
print(Persona2)
print(Persona3)

#para acceder al contador persona
print(f'El contador actual es: {Persona.contador_personas}')