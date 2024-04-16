class ClaseEjemplo:
    #Se asocia al objeto mismo no asi, es decir es una variable de clase, esto fuera del metodo __init__
    variable_ejemplo = 'Hola Mundo'
    #Al crear un objeto de esta clase, y se ejecuta el metodo init, se crea e inicializa la variable_de_instancia!
    def __init__(self, variable_de_instancia):
        self.variable_de_instancia = variable_de_instancia
        
#Se asocia a la clase misma no a un objeto
print(ClaseEjemplo.variable_ejemplo)
#Se crea/instancia el objeto para se accedido.
miClase = ClaseEjemplo('Valor de instancia')
print(miClase.variable_de_instancia)    
#Desde el objeto creado, el mismo se encuentra en memoria por lo cual es posible acceder.
test = miClase.variable_ejemplo
print(test)

#Al crear otra instancia es posible tener un valor diferente
test1=ClaseEjemplo('Helloooo!!!')
print(test1.variable_de_instancia)
print(test1.variable_ejemplo)