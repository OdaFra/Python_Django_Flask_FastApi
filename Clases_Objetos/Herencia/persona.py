# Herencia desde una clase
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def __str__(self):
        return f'La persona tiene de nombre: {self.nombre}, edad: {self.edad}'


# Aplicando herencia desde una clase hija, si se desea agrear mas clase padre se deben ir colocando separadas por comas.
class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self.sueldo = sueldo

    def __str__(self):
        return f'{super().__str__()}, y sueldo: {self.sueldo}'
    # def mostrarDetalle(self):
    #     print(f"Los datos del empleado son: {self.nombre}, {self.edad}, {self.sueldo}")


print('Creacion de objetos'.center(50,'-'))
empleado = Empleado('Nahomi', 7, 3500)
#empleado.mostrarDetalle()