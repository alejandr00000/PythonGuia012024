'''
15.	Cree un programa que reciba el radio de una esfera y, cuando éste sea no negativo, calcule su área 
o volumen, de acuerdo a lo ingresado por el usuario.
'''

import math

eleccion = input('Este programa calcula el área o volumen de una esfera.\nIngrese 1 si desea calcular el área o 2 si desea calcular el volumen: ')

match eleccion:
    case '1':
        radio = float(input('ingrese el radio del círculo: '))
        result = 4*math.pi*radio**2
        print(f'El Área de las esfera es {result}')
    case '2':
        radio = float(input('ingrese el radio del círculo: '))
        result = 4/3*math.pi*radio**3
        print(f'El volumen de la esfera es {result}')
    case _:
        print('Error. Debe ingresar 1 o 2.')