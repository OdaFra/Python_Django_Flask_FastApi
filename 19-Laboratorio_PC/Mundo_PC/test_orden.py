from Teclado import Teclado
from Raton import Raton
from Monitor import Monitor
from Computadora import Computadora
from Orden import Orden


if __name__ == '__main__':
    teclado = Teclado('Redragon', 'wireless')
    raton = Raton('MasterCooler', 'wireless')
    monitor = Monitor('Asus', 27)
    compurtadora=Computadora('Gamer', monitor, teclado, raton)
    # print(compurtadora)
    teclado1 = Teclado('Corsair', 'wireless')
    raton1 = Raton('Razer', 'wireless')
    monitor1 = Monitor('Asus', 32)
    compurtadora1=Computadora('Gamer', monitor1, teclado1, raton1)
    # print(compurtadora1)
    
    computadoras = [compurtadora, compurtadora1]
    orden = Orden(computadoras)
    print(orden)