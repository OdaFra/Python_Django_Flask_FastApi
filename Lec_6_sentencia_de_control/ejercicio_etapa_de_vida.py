edad =int(input('Proporciona tu edad: '))
etapaDeVida = None

if  0<=  edad < 10:
    etapaDeVida= 'La infancia es increible'
elif  10 <= edad < 20:
    etapaDeVida = 'Muchos cambios y muchos estudios'
elif 20 <=  edad < 30:
    etapaDeVida = 'Amor y comienza el trabajo'
else:
    etapaDeVida ='Etapa de la vida no reconocida'
print(f'La edad es {edad}, y se encuentra en la etapa de {etapaDeVida}')