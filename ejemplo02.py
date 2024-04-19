'''
Cree un programa que calcule la suma de dos números dados por el usuario, mostrando el resultado.
'''

number01 = float(input('Ingrese el primer número que quiere sumar: '))
number02 = float(input('Ingrese el segundo número que quiere sumar: '))

sum = number01 + number02
message = f'{number01} + {number02} = {sum}'
print(message)
