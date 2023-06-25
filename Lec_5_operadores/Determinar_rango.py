# valor = int(input('Proporcione un valor : '))
# valorMin = 0;
# valorMax = 5;

# # AND
# if (valor >= valorMin and valor <= valorMax):
#     print(f'Se encuentra dentro del rango, y el valor es: {valor}')
# else:
#     print(f'Se encuentra fuera del rango, y el valor es: {valor}')

# # OR
# vacaciones = False
# diasDescanso = False

# if vacaciones or diasDescanso:
#     print('Puede asistir')
# else:
#     print('Tiene deberes')

# NOT
# vacaciones = False
# diasDescanso = False

# if not  (vacaciones or diasDescanso):
#     print('Puede asistir')
# else:
#     print('Tiene deberes')

#Comprobar rango de 20 a 30
edad = int(input('Introduce tu edad: '))
# vientes = edad >= 20 and edad < 30
# trientas = edad >= 30 and edad < 40

# if vientes or trientas:
#     print('Te encuentras en el rango de los 20\'s y los 30\'s')
# else:
#     print('Te encontras en el rango menor de los 20')
    
if (   20<= edad < 30) or ( 30<= edad <40):
    print('Te encuentras en el rango de los 20\'s y los 30\'s')
else:
    print("No está dentro de los 20's ni 30's")