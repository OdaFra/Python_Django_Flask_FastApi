archivo = open('./21-Manejo de archivos/prueba.txt', 'r')
# print(archivo.read())

#Leer algunos caracteres!
# print(archivo.read(5))
# print(archivo.read(6))

#Leer lineas completas
# print(archivo.readlines(1))

#Iteramos cada lineas
# for linea in archivo:
#     print(f'Las lineas son: {linea}')

#Leer todas las lineas
# print(archivo.readlines())

#Leer solo una linea de la lista
# print(archivo.readlines()[2])

#Abrimos un nuevo archivo
#a - Anexamos informacion
archivo2 = open('./21-Manejo de archivos/pruebaCopia.txt', 'r')
archivo2.write(archivo.read())

archivo.close()
archivo2.close()
print('Se ha finalizado el proceso')

