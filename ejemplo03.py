'''
Realice un programa que calcule el área o el perímetro de un círculo, de acuerdo a lo solicitado por el usuario.
Debe pedir el radio del círculo al usuario y arrojar un mensaje de error cuando el valor ingresado sea negativo.
'''
import math

eleccion = input('Este programa calcula áreas y perímetros de círculos.\nIngrese 1 si desea calcular el área y 2 si desea calcular el perímetro: ')

#Usando if

if (eleccion == '1'):
    radio = float(input('Ingrese el radio del círculo: '))
    result = math.pi*radio**2
    print(f'El área del círculo de radio {radio} es igual a {result}')
elif (eleccion == '2'):
    radio = float(input('Ingrese el radio del círculo: '))
    result = 2*math.pi*radio
    print(f'El perímetro del círculo de radio {radio} es igual a {result}')
else:
    result = 'Error. Debes ingresar 1 o 2.'
    print(result)

#Usando match

match eleccion:
    case '1':
        radio = float(input('Ingrese el radio del círculo: '))
        result = math.pi*radio**2
        print(f'El área del círculo de radio {radio} es igual a {result}')
    case '2':
        radio = float(input('Ingrese el radio del círculo: '))
        result = 2*math.pi*radio
        print(f'El perímetro del círculo de radio {radio} es igual a {result}')
    case _:
        result = 'Error. Debes ingresar 1 o 2.'
        print(result)




