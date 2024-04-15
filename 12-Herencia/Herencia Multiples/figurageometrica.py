#ABC = Abstract Base Clase
from abc import ABC, abstractmethod

class FiguraGeometrica(ABC):
    def __init__(self, alto, ancho):
        # Encapsulamos los atributos con el _
        if  self._validar_valor(alto): #0 < alto <= 10:
            self._alto = alto
        else:
            self._alto = 0
            print(f'Valor erroneo para el alto: {alto}')
        if  self._validar_valor(ancho): #0 < ancho <=10:
            self._ancho = ancho
        else:
            self._ancho = 0
            print(f'Valor erroneo para el ancho: {ancho}')

    # Agregamos get y set
    @property
     # Add method
    # GET
    def alto(self):
        return self._alto

    @alto.setter
    # SET
    def alto(self, alto):
        if self._validar_valor(alto):
            self._alto = alto
        else:
            print(f'Valor erroneo para el alto: {alto}')
    
    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, ancho):
        if self._validar_valor(ancho):
            self._ancho = ancho
        else:
            print(f'Valor erroneo para el alto: {ancho}')
    
    @abstractmethod
    def calcular_area(self):
        pass

    def __str__(self):
        return f"Figura Geometrica [Alto: {self._alto}, Ancho: {self._ancho}]"

    def _validar_valor(self, valor):
        return True if 0 < valor < 10 else False