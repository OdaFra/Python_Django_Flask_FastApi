from ManejoArchivo import ManejoArchivos
# with open('./21-Manejo de archivos/prueba.txt','r') as archivo:
#     print(archivo.read())
with ManejoArchivos('./21-Manejo de archivos/prueba.txt') as archivo:
    print(archivo.read())