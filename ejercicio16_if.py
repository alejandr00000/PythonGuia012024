'''
16.	Cree un programa que reciba tres calificaciones e imprima su promedio, siempre que las calificaciones 
estén entre 1,0 y 7,0. De lo contrario, debe imprimir un mensaje de error.
'''

nota01 = float(input('Este programa calcula el promedio de tres calificaciones. \nIngrese la primera calificación: '))
nota02 = float(input('Ingrese la segunda calificación: '))
nota03 = float(input('Ingrese la tercera calificación: '))

if (1 <= nota01 <= 7 and 1 <= nota02 <= 7 and 1 <= nota03 <=7):
    promedio = (nota01 + nota02 + nota03)/3
    print(f'El promedio es {promedio}')
else:
    print(f'Error. Las calificaciones deben estar entre 1 y 7')


#Si se quiere mostrar un mensaje en pantalla cuando los usuarios ingresen algun caracter que no sea número

'''
try:
    nota01 = float(input('Este programa calcula el promedio de tres calificaciones. \nIngrese la primera calificación: '))
    nota02 = float(input('Ingrese la segunda calificación: '))
    nota03 = float(input('Ingrese la tercera calificación: '))

    if (1 <= nota01 <= 7 and 1 <= nota02 <= 7 and 1 <= nota03 <=7):
        promedio = (nota01 + nota02 + nota03)/3
        print(f'El promedio es {promedio}')
    else:
        print(f'Error. Las calificaciones deben estar entre 1 y 7')
    
except ValueError:
    print('Error. Se debe ingresar números')
'''
