from Empleado import Empleado
from Gerente import Gerente

def imprimir_detalles(objeto):
    # print(objeto)
    print(type(objeto))
    print(objeto.mostrar_detalles())
    #Validacion si el artributo pertenece al objeto por ejemplo departamento a Gerente
    if isinstance(objeto, Gerente):
        print(objeto.departamento)

empleado = Empleado('Juan', 2200)
imprimir_detalles(empleado)

gerente = Gerente('Alberto', 3000, 'Mecanica')
imprimir_detalles(gerente)

