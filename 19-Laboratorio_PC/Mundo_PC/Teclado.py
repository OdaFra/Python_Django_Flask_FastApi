from DispositivoEntrada import DispositivoEntrada

class Teclado(DispositivoEntrada):
    contador_Teclados=0
    def __init__(self, marca, tipo_entrada):
        Teclado.contador_Teclados+=1
        self._id_Teclado=Teclado.contador_Teclados
        super().__init__(marca, tipo_entrada)
    
    def __str__(self):
        return f'Id: {self._id_Teclado}, Marca: {self._marca}, tipo: {self._tipo_entrada}'

if __name__=='__main__':
    Teclado1 = Teclado('HP','Wireless')
    print(Teclado1)
    Teclado2 = Teclado('Redragon','Wireless')
    print(Teclado2)