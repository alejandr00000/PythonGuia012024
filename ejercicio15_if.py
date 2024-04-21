'''
15.	Cree un programa que reciba el radio de una esfera y, cuando éste sea no negativo, calcule su área 
o volumen, de acuerdo a lo ingresado por el usuario.
'''
import math

eleccion = input('Este programa calcula el área o volumen de una esfera.\nIngrese 1 si desea calcular el área o 2 si desea calcular el volumen: ')

if (eleccion == '1'):
    #En este código no se verifica que el radio deba ser no negativo. Si quiere, agregue más líneas para poder verificarlo.
    radio = float(input('ingrese el radio del círculo: '))
    result = 4*math.pi*radio**2
    print(f'El Área de las esfera es {result}')
elif (eleccion == '2'):
    radio = float(input('ingrese el radio del círculo: '))
    result = 4/3*math.pi*radio**3
    print(f'El volumen de la esfera es {result}')
else:
    print('Error. Debe ingresar 1 o 2.')
