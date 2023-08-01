def imprimirNroRecursivo(numero):
    if numero >=1:
        print(numero)
        return imprimirNroRecursivo(numero-1)
    elif numero == 0:
        print('El valor es 0')
    elif numero<=0:
        print('Valor incorrecto..')

#Testing
numero = 0
res=imprimirNroRecursivo(numero)
print(res)