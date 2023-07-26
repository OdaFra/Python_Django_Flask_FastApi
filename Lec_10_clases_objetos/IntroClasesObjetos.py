#Nueva clase Persona
class Persona:
    #definimos los parametros para agregar a los atributos de la clase
    def __init__(
        self,
        nombre,
        apellido,
        edad,
    ):
    # Atributos
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
    # Creacion de metodo    
    def  mostrarDetalle(self):
        print(f'Persona:{self.nombre}, {self.apellido}, {self.edad}')



#Nuevo Objecto
person = Persona('Naho', 'Ramirez','7')
#Accedemos a los atributos de la clase
# print(f'Su datos son {person.nombre}, {person.edad}')

# person.nombre='Montse'
# person.apellido='Iglesias'

# print(f'Su datos son {person.nombre}, {person.apellido}')

person1=Persona('Noah','Ramirez', 25)
# print(f'Su datos son {person1.nombre}, {person1.apellido}')

## Imprimir metodo
person.mostrarDetalle()
person1.mostrarDetalle()


#Llamar directamente al metodo desde la clase
Persona.mostrarDetalle(person)
