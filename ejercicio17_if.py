'''
17.	Cree un programa que pida un número entero al usuario. Luego de verificar que es un número entero, 
se debe calcular su raíz cuadrada e indicar si ésta es racional o irracional.
'''

numero = float(input('Ingrese un número entrero: '))
numero_entero = int(numero)

if (numero == numero_entero):
    raiz_cuadrada = numero ** (1/2)
    parte_decimal = raiz_cuadrada - int(raiz_cuadrada)

    if (parte_decimal == 0):
        print(f'La raíz cuadrada de {numero} es racional')
    else:
        print(f'La raíz cuadrada de {numero} es irracional')

else:
    print('Error. Debe ingresar un número entero')


