class ManejoArchivos:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def __enter__(self):
        print('Obtenemos el recurso'.center(60, '*'))
        self.nombre = open(self.nombre, 'r', encoding='utf8')
        return self.nombre

    def __exit__(self,typeException, valueException, traceException):
        print('Cerramos el recurso'.center(60, '*'))
        if self.nombre:
            self.nombre.close()
        