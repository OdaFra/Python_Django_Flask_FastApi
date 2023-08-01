#
# Calcular el area y perimetro de un rectangulo

print('Inicio del programa')
alto = int(input('Proporcione el alto: '))
ancho = int(input('Proporcione el ancho: '))
area = alto * ancho
perimetro = (alto + ancho) * 2

print(f'El area es {area}, y el perimetro es {perimetro}')