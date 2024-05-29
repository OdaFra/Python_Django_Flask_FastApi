from dominio.Pelicula import Pelicula
from servicio.CatalogoPelicula import CatalogoPeliculas as cp

opcion = None

while opcion !=4:
    try:
        print('Opciones:   ')
        print('1. Agregar Pelicula')
        print('2. Listar Peliculas')
        print('3. Eliminar Peliculas')
        print('4. Salir')
        opcion = int(input('Escibre tu opcion (1-4):'))
        
        #Agregar Pelicula
        if opcion == 1:
            nombrePelicula = input('Proporcione el nombre de la pelicula: ')
            pelicula = Pelicula(nombrePelicula)
            cp.agregarPelicula(pelicula)
        elif opcion == 2:
            cp.listarPeliculas()
        elif opcion == 3:
            cp.eliminarPeliculas()

    except Exception as e:
        print(f'Ha ocurrido un error: {e}')
        opcion=None
else:
    print('Ha salido del programa....')