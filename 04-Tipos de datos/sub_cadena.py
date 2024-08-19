valor = 'Hola Mundo'
sub_cadena = valor[5:-1]
print(sub_cadena)

#Metodo find - Devuelve el indice de valor a buscar
varfind = valor.find('Mundo')
print(varfind) # Devuelve el indice del str

#Reemplazar str - reemplaza un valor por otro, es Case Sensitive
nuevo = valor.replace('Mundo','mundo a todos')
print (nuevo)

#Funcion Split - Permite dividir una cadena en una lista de subcadena basada en el caracter separador
datos = 'Juan, 33, PY'
lista = datos.split(',')
print(f'La lista es: {lista}')
