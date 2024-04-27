
class Monitor:
    contador_monitores=0
    def __init__(self, marca, tamanho):
        Monitor.contador_monitores+=1
        self._id_monitor = Monitor.contador_monitores
        self._marca = marca
        self._tamanho = tamanho

    def __str__(self):
        return f'Id: {self._id_monitor}, Marca: {self._marca}, tamanho:{self._tamanho}'


if __name__ == '__main__':
    monitor1= Monitor('LG', 27)
    monitor2= Monitor('Samsung', 24)
    print(f'Los monitores son: {monitor1} \n{monitor2}')