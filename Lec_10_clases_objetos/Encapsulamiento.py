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
        self._apellido = apellido
        self._edad = edad

#Manejo de GETTER y SETTER
    # Metodo Get
    @property
    def getNombre(self):
        return self._nombre

    # Metodo setter
        #Si se llegase a comentar esta seccion corresponde a una variable de solo lectura.
    @getNombre.setter
    def setNombre(self, nombre):
        self._nombre = nombre

    @property
    def getApellido(self):
        return self._apellido
    
    @getApellido.setter
    def setApellido(self, apellido):
        self._apellido=apellido

    @property
    def getEdad(self):
        return self._edad
    
    @getEdad.setter
    def setEdad(self, edad):
        self._edad = edad

    # Creacion de metodo
    def mostrarDetalle(self):
        print(f"Persona:{self._nombre}, {self._apellido}, {self._edad}")

    def __del__(self):
        print(f'Persona {self._nombre}, {self._apellido}')

# Nuevo Objecto
person = Persona("Naho", "Ramirez", 7)
# En python es posible aplicar esto pero desde el otros lenguajes no!
# person._nombre='Vale'

if __name__ =='__main__':
    person.setNombre='Oscar'
    person.setApellido='Franco'
    person.setEdad=32
    person.mostrarDetalle()
