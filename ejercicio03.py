'''
3.	Escriba un programa que pregunte el nombre completo del usuario en la consola y después muestre 
por pantalla el nombre completo del usuario tres veces, una con todas las letras minúsculas, otra con 
todas las letras mayúsculas y otra solo con la primera letra del nombre y de los apellidos en mayúscula. 
El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera.
'''

name = input('Ingrese su nombre completo: ')
name_lower = name.lower()
print(name_lower)
name_upper = name.upper()
print(name_upper)
name_title = name.title()
print(name_title)