'''
11.	Escriba un programa que pida un número que representa una temperatura en Celsius. Imprime el valor 
de la misma temperatura en Fahrenheit.
'''

celsius = float(input('Ingrese la temperatura en grados celsius: '))
fahrenheit = celsius * 9/5 + 32
mensaje = f'Temperatura °C: {celsius}\nTemperatura °F: {fahrenheit}'
print(mensaje)