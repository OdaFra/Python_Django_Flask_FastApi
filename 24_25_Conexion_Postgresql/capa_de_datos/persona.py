from loggers.logger import log


class Persona:
    def __init__(self, id_persona=None, nombre=None, apellido=None, email=None):
        self.id_persona = id_persona
        self.nombre = nombre
        self.apellido = apellido
        self.email = email

    # Metodo STR
    def __str__(self):
        return f"""
        Id Persona: {self.id_persona}, Nombre: {self.nombre}, 
        Apellido: {self.apellido}, Email: {self.email}
        
    """


@property
# GETTER
def id_persona(self):
    return self._id_persona


# SETTER
@id_persona.setter
def id_persona(self, id_persona):
    self._id_persona = id_persona


@property
def nombre(self):
    return self._nombre


@nombre.setter
def nombre(self, nombre):
    self._nombre = nombre


@property
def apellido(self):
    return self._apellido


@apellido.setter
def apellido(self, apellido):
    self._apellido = apellido


@property
def email(self):
    return self._email


@email.setter
def email(self, email):
    self._email = email


if __name__ == "__main__":
    persona = Persona(1, "Naho", "Ramirez", "nr@test.com")
    log.debug(persona)
    # Simular un insert
    people = Persona(nombre="Benja", apellido="Ramirez",email= "br@test.com")
    log.debug(people)
    #Simular delete
    person = Persona(id_persona=1)
    log.debug(person)