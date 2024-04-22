class Producto:
    contador_producto = 0
    
    def __init__(self, nombre, precio):
        Producto.contador_producto+=1
        self._id_producto = Producto.contador_producto
        self._nombre= nombre
        self._precio = precio

#Falta agregar un getter y setter         

    @property
    def precio(self):
        return self._precio

#Metodo STR
    def __str__(self):
        return f'Id Producto:{self._id_producto}, Nombre:{self._nombre}, Precio:{self._precio}'

#Permite evaluar esta prueba si se esta ejecutando desde este mismo archivo, no asi desde otro.
if __name__ == '__main__':
    producto1 = Producto('Jeans', 120.2)        
    producto2 = Producto('Camisa', 110.5)      
    print(producto1)
    print(producto2)