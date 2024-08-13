# NaN -> Not a Number (no es un numero)
# NaN -> No es sensible a mayusculas/minusculas
# NaN -> tipo de dato indefinido

import math as math
from decimal import Decimal

a = float('NaN')

print('Valor a: {}'.format(a))
print (f'Es NaN (not a number)? :{math.isnan(a)}')

b = Decimal('NaN')
print (f'Es NaN (not b number)? :{math.isnan(b)}')