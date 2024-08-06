import sys
import os

# Para poder ubicar la ruta del archivo a importar
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from loggers.logger import log 

class Usuario:
    def __init__(self, id_user=None, username=None, password=None):
        self._id_user = id_user
        self._username = username
        self._password = password
    
    def __str__(self):
        return f'''Usuario: 
        [id: {self._id_user} - username: {self._username} - password: {self._password}]
        '''
    ##id_user
    #getter
    @property
    def id_user(self):
        return self._id_user
    
    #setter
    @id_user.setter
    def id_user(self, id_user):
         self._id_user = id_user

##username
    #getter
    @property
    def username(self):
        return self._username
    
    #setter
    @username.setter
    def username(self, username):
         self._username = username

##password
    #getter
    @property
    def password(self):
        return self._password
    
    #setter
    @password.setter
    def password(self, password):
         self._password = password



if __name__ == "__main__":
    usuario = Usuario(1, "Naho", "1234")
    log.debug(usuario)
    # Simular un insert
    people = Usuario(username="Benja",password='12345')
    log.debug(people)
    #Simular delete
    person = Usuario(id_user=1)
    log.debug(person)