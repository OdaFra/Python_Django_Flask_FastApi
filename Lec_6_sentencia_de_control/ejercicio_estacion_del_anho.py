mes = int(input('Proporciona mes del anho del 1 al 12: '))
estacion = None

if mes == 12 or mes == 1 or mes == 2:
    estacion = 'Verano'
elif mes == 3 or mes == 4 or mes == 5:
    estacion = 'Otonho'
elif mes == 6 or mes == 7 or mes == 8:
    estacion = 'Invierno'
elif mes == 9 or mes == 10 or mes ==11:
    estacion= 'Primavera'
else:
    estacion= 'Mes incorrecto'
print(f'Para el mes {mes}, la estacion es {estacion}')