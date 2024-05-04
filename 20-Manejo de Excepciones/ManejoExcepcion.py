from NumerosIdenticosExcepcion import NumerosIdenticosException

result=None
a = int(input('Ingrese el primer numero: '))
b = int(input('Ingrese el segundo numoro: '))
try: 
    if a == b:
        raise NumerosIdenticosException('Numeros identicos')
    result = a /b
except ZeroDivisionError as e :
  print(f'An exception occurred: {e}, {type(e)}')
except TypeError as e:
    print(f'An exception occurred: {e}, {type(e)}')
except Exception as e:
    print(f'An exception occurred: {e}, {type(e)}')
else:
    print('No se presento ningun caso de exception!')
finally:
    #Siempre se va a ejecutar
    print('Bloque finally...')


print(f'El resultado es: {result}')
print(f'Continuamos.....')
