nro = int(input('Proporciona un valor de 1 al 3: '))
nroTexto=''
if nro ==1:
    nroTexto = 'Numero uno'
elif nro==2:
    nroTexto ='Numero dos'
elif nro==3:
    nroTexto='Numero tres'
else:
    nroTexto='Valor proporcionado no corresponde al rango'

print(f' El nro proporcionado es {nro} - {nroTexto}')