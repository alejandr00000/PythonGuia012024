'''
10.	Escriba un programa que pida dos números al usuario e imprima en pantalla el valor de la suma, resta, 
multiplicación y división de los números. ¿Qué problema podría haber con el programa?
'''

num01 = float(input('Ingrese el primer número: '))
num02 = float(input('Ingrese el segundo número: '))

suma = num01 + num02
resta = num01 - num02
multiplicacion = num01 * num02
division = num01 / num02

mensaje = f'{num01} + {num02} = {suma}\n{num01} - {num02} = {resta}\n{num01} * {num02} = {multiplicacion}\n{num01} / {num02} = {division}'

print(mensaje)