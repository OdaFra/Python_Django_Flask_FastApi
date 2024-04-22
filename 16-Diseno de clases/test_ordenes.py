from Producto import Producto
from Order import Order
    
producto1 = Producto('Jeans', 120.2)        
producto2 = Producto('Camisa', 110.5)
producto3 = Producto('Short', 95.5)       
producto4 = Producto('Gorra', 45.5)

lista_productos1= [producto1, producto2]
lista_productos2 = [producto3, producto4]
orden1 = Order(lista_productos1)
orden1.agregar_producto(producto3)
orden1.agregar_producto(producto4)
print(orden1)
#Total del la orden 1
print(f'Total de la orden 1:{ orden1.calcular_total()}')
orden2 = Order(lista_productos2)
print(orden2)
#Total del la orden 2
print(f'Total de la orden 2:{ orden2.calcular_total()}')