from Teclado import Teclado 
from Raton import Raton
from Monitor import Monitor

class Computadora:
    contador_compurtadoras=0
    def __init__(self, nombre, monitor, teclado, raton):
        Computadora.contador_compurtadoras+=1
        self._id_conputadora = Computadora.contador_compurtadoras
        self._nombre = nombre
        self._monitor = monitor
        self._teclado = teclado
        self._raton = raton
    
    def __str__(self):
        return f'''
    
        {self._nombre}:{self._id_conputadora}
        Monitor:{self._monitor}
        Teclado:{self._teclado}
        raton:{self._raton}
        
        '''


if __name__ == '__main__':
    teclado = Teclado('Redragon', 'wireless')
    raton = Raton('MasterCooler', 'wireless')
    monitor = Monitor('Asus', 27)
    compurtadora=Computadora('Gamer', monitor, teclado, raton)
    print(compurtadora)
    teclado1 = Teclado('Corsair', 'wireless')
    raton1 = Raton('Razer', 'wireless')
    monitor1 = Monitor('Asus', 32)
    compurtadora1=Computadora('Gamer', monitor1, teclado1, raton1)
    print(compurtadora1)