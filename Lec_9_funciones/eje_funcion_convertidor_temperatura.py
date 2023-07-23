#Convertidor de temperatura de C a F

def celsius_fahrenheit(celsius):
    return ((celsius*9)/5)+32

def fahrenheit_celisus(fahrenheit):
    return (fahrenheit-32) * 5 / 9 

temperaturaCelsius=float(input('Proporcione su valor en celsius: '))
resFahrenheit = celsius_fahrenheit(temperaturaCelsius)
print(f'{temperaturaCelsius} C a F : {resFahrenheit:.2F}')

temperaturaFahrenheit=float(input('Proporcione su valor en fahrenheit: '))
resCelsius = fahrenheit_celisus(temperaturaFahrenheit)
print(f'{temperaturaFahrenheit} F a c : {resCelsius:.2F}')