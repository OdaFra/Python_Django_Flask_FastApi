from DispositivoEntrada import DispositivoEntrada

class Raton(DispositivoEntrada):
    contador_ratones=0
    def __init__(self, marca, tipo_entrada):
        Raton.contador_ratones+=1
        self._id_raton=Raton.contador_ratones
        super().__init__(marca, tipo_entrada)
    
    def __str__(self):
        return f'Id: {self._id_raton}, Marca: {self._marca}, tipo: {self._tipo_entrada}'

if __name__=='__main__':
    raton1 = Raton('HP','Wireless')
    print(raton1)
    raton2 = Raton('Redragon','Wireless')
    print(raton2)