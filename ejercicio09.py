'''
9.	Cree un programa que pida un número al usuario e imprima en pantalla el antecesor y el sucesor del número.
'''

num = int(input('Ingrese un número entero: '))
antecesor = num - 1
sucesor = num + 1

mensaje = f'Número: {num}\nAntecesor: {antecesor}\nSucesor: {sucesor}'
print(mensaje) 