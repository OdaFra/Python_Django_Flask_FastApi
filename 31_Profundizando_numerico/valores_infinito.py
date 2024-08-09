#Manejop de valores infinitos

import math as m
from decimal import Decimal

infinito_positivo = float('inf')
# print(f'Infinito positivo: { infinito_positivo}')
# print(f'Es infinito: {m.isinf( infinito_positivo)}')

infinito_negativo = float('-inf')
# print(f'Infinito positivo: { infinito_negativo}')
# print(f'Es infinito: { m.isinf( infinito_negativo)}')

#Modulo de Math
infinito_positivo = m.inf
# print(f'Infinito positivo: { infinito_positivo}')
# print(f'Es infinito: {m.isinf( infinito_positivo)}')

infinito_negativo= -m.inf
# print(f'Infinito negativo: { infinito_negativo}')
# print(f'Es infinito negativo: { m.isinf( infinito_negativo)}')

#Modulo Decimal
infinito_positivo = Decimal('Infinity')
print(f'Infinito negativo: { infinito_positivo}')
print(f'Es infinito negativo: { m.isinf( infinito_positivo)}')
