'''
12.	Escriba un programa que pida el tiempo en horas con decimales e imprima el mismo tiempo, pero con 
horas:minutos:segundos.
'''

hora_decimal = float(input('Ingrese tiempo en horas utilizando decimales: '))
horas = int(hora_decimal)
minutos_decimal = (hora_decimal - horas)*60
minutos = int(minutos_decimal)
segundos_decimal = (minutos_decimal - minutos)*60
segundos = int(segundos_decimal)

mensaje = f'{hora_decimal} horas = {horas} horas, {minutos} minutos, {segundos} segundos'

print(mensaje)
