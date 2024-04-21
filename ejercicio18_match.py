'''
18.	Cree un programa que pida dos números al usuario y la operatoria que quiere realizar (suma, resta, 
multiplicación y división). Luego, que imprima el resultado en pantalla.
'''

print('Este programa calcula la operatoria entre dos números')
num01 = float(input('Ingrese el primer número: '))
num02 = float(input('Ingrese el segundo número: '))

operatoria = input('Para sumar ingrese 1. Para restar, 2. Para multiplicar, 3. Para dividir, 4.: ')

match operatoria:
    case '1':
        result = num01 + num02
        print(f'{num01} + {num02} = {result}')
    case '2':
        result = num01 - num02
        print(f'{num01} - {num02} = {result}')
    case '3':
        result = num01 * num02
        print(f'{num01} * {num02} = {result}')
    case '4':
        result = num01 / num02
        print(f'{num01} / {num02} = {result}')
    case _:
        print('Error. Debe ingresar 1, 2, 3 o 4')
