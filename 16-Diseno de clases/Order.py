from Producto import Producto

class Order:
    contador_ordenes=0
    
    def __init__(self, productos):
        Order.contador_ordenes+=1
        self._id_order = Order.contador_ordenes
        self._productos = list(productos)
    
    def agregar_producto(self, producto):
        self._productos.append(producto)
    
    def calcular_total(self):
        total = 0
        for producto in self._productos:
            total +=producto.precio
        return total
    
    def __str__(self):
        productos_str=''
        for producto in self._productos:
            productos_str +=producto.__str__() + ' | '
        
        return f'Orden:{self._id_order}, \nProductos:{productos_str}'
    
if __name__=='__main__':
    producto1 = Producto('Jeans', 120.2)        
    producto2 = Producto('Camisa', 110.5)       
    lista_productos= [producto1, producto2]
    orden1 = Order(lista_productos)
    print(orden1)
    orden2 = Order(lista_productos)
    print(orden2)
    