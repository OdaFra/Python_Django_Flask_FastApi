#La clase se carga en memoria la primera vez que se crea un objeto.

class ClaseEjemplo:
    #Se asocia al objeto mismo no asi, es decir es una variable de clase, esto fuera del metodo __init__
    variable_claseEjemplo = 'Hola Mundo'
    #Al crear un objeto de esta clase, y se ejecuta el metodo init, se crea e inicializa la variable_de_instancia!
    def __init__(self, variable_de_instancia):
        self.variable_de_instancia = variable_de_instancia

    #Metodos estaticos
    #No puede acceder a las variables de instancias con relacion al parametro de self.
    #No recibi ninguna informacion de la clase misma, por eso podemos decir que no tiene directamente con nuestra clase.
    @staticmethod
    def metodo_estatico():
        #acceder de manera indirecta a la clase
         print(ClaseEjemplo.variable_claseEjemplo)
    
    #Un metodo de clase si recibe un contexto de clase 
    @classmethod
    def metodo_clase(cls):
        cls.variable_claseEjemplo = 'Golang'
        print(f'{cls.variable_claseEjemplo}, test')
    
    #Metodo de instancia, lo cual es de contexto dinamico y puede acceder a metodos de clases como estaticos
    def metodo_instancia(self):
        self.metodo_clase()
        self.metodo_estatico()
        print(self.variable_claseEjemplo)
        print(self.variable_de_instancia)


        
#Se asocia a la clase misma no a un objeto
print(ClaseEjemplo.variable_claseEjemplo)
#Se crea/instancia el objeto para se accedido.
miClase = ClaseEjemplo('Valor de instancia')
print(miClase.variable_de_instancia)    
#Desde el objeto creado, el mismo se encuentra en memoria por lo cual es posible acceder.
test = miClase.variable_claseEjemplo
print(test)

#Crear variables y asocialar a la clase en el vuelo o ejecucion del programa
ClaseEjemplo.variable_de_instancia2 = 'Goo!'

#Al crear otra instancia es posible tener un valor diferente
test1=ClaseEjemplo('Helloooo!!!')
print(test1.variable_de_instancia)
print(test1.variable_claseEjemplo)
print(ClaseEjemplo.variable_de_instancia2)
print(miClase.variable_de_instancia2)
print(test1.variable_de_instancia2)

#Llamar al metodo estatico 
ClaseEjemplo.metodo_estatico()

#Llamar al metodo de clase agregado
ClaseEjemplo.metodo_clase()
#Crear un objeto y acceder al metodo de clase
miObjeto = ClaseEjemplo('Mi objeto de prueba')
# print(miObjeto)
miObjeto.metodo_clase()
miObjeto.metodo_instancia()