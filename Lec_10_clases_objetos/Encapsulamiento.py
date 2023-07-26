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
        self._nombre = nombre
        self.apellido = apellido
        self.edad = edad

#Manejo de GETTER y SETTER
    # Metodo Get
    @property
    def getNombre(self):
        print("Llamando metodo get..")
        return self._nombre

    # Metodo setter
    @getNombre.setter
    def setNombre(self, nombre):
        print("Llamando metodo set..")
        self._nombre = nombre

    # Creacion de metodo
    def mostrarDetalle(self):
        print(f"Persona:{self._nombre}, {self.apellido}, {self.edad}")


# Nuevo Objecto
person = Persona("Naho", "Ramirez", 7)
# En python es posible aplicar esto pero desde el otros lenguajes no!
# person._nombre='Vale'

person.setNombre='Oscar'
print(person.getNombre)
