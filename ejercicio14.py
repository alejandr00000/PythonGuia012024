'''
14.	Cree un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, 
y muestre por pantalla el capital obtenido en la inversión (busque fórmula de interés compuesto).
'''

cantidad_inicial = int(input('Indique el monto que desea invertir: '))
interes = float(input('Indique la tasa de interés: '))
#Cambié los años por meses y se asume que la tasa de interés es mensual
tiempo = float(input('Indique la cantidad de meses que desea invertir su dinero: '))
cantidad_final = int(cantidad_inicial*(1 + interes)**tiempo)

mensaje = f'El capital obtenido en la inversión es ${cantidad_final}'
print(mensaje)