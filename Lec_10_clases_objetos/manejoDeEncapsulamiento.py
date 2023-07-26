# Encapsulacion
class Persona:
    # definimos los parametros para agregar a los atributos de la clase
    def __init__(
        self,
        nombre,
        apellido,
        edad,
    ):
        # Atributos
        # Encapsulamiento (atributo privado) 
        self.__nombre = nombre
        self.apellido = apellido
        self.edad = edad

    # Creacion de metodo
    def mostrarDetalle(self):
        print(f"Persona:{self.__nombre}, {self.apellido}, {self.edad}")


# Nuevo Objecto
person = Persona("Naho", "Ramirez",7)
#En python es posible aplicar esto pero desde el otros lenguajes no!
# person._nombre='Vale'
person.__nombre='Vale'
person1 = Persona("Noah", "Ramirez", 25)

## Imprimir metodo
person.mostrarDetalle()
person1.mostrarDetalle()


# Llamar directamente al metodo desde la clase
Persona.mostrarDetalle(person)
