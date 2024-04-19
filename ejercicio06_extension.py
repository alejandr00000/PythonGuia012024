'''
Extensión: Realice el mismo ejercicio, pero ahora permite ingresar cualquier dominio al usuario y lo 
reemplaza por lincolncollege.cl.
'''

initial_email = input('Ingrese un correo electrónico: ')

#No les mostré cómo encontrar la posición de un caracter en especial
#Busca la ubicación del caracter '@'
char = initial_email.find('@')
final_email = initial_email[0:char] + '@lincolncollege.cl'
print(final_email)