print('Proporcione los siguientes datos del libro:')
nombre = input('Proporciones el nombre del libro: ')
idLibro = int(input('Proporcione un ID: '))
precio = float(input('Proporcione un precio: '))
envio = input('Indica si el envio es gratis (TRUE/FALSE) :')

if envio == 'True':
    envio=True
elif envio == 'False':
    envio = False
else:
    envio='Valor incorrecto, debe escribir True o False'

print(f'''
    nombre : {nombre}
    Id : {idLibro}
    precio: {precio}
    envio: {envio}
''')

# print(f'El nombre del libro es {nombre}')
# print(f'El id del libro es {idLibro}')
# print(f'El precio es {precio}')
# print(f'El envio es gratuito {envio}')