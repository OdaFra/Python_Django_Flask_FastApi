def listaTerminos(**kwargs):
    for llave, valor in kwargs.items():
        print(f'{llave}: {valor}')
        

listaTerminos(IDE='Int. Dev Env', PK='Primary Key')