#Profundizando tipo float
a = 3.0
print(f'a: {a:.3f}')

#Constructor de tipo float
b = float(10)
#Se puede aplicar un string, a esto se le conoce como sobre carga
s = float('10')
print(f'numerico: {b:.3f}')
print(f'string: {s:.2f}')

#Notaacion exponencial (valores positivos o negativos)
ex= 35e2
nex= 3e-5
print(f'exponencial: {ex:.2f}')
print(f'exp negativo: {nex:.5f}')

#Cualquier calculo que involucre float, el resultado sera a float
#Suma
s= 1.5 + 2 
print(f'suma: {s}')
