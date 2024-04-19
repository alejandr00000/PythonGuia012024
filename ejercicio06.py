'''
6.	Escriba un programa que pregunte un correo electrónico @gmail.com del usuario y muestre por pantalla 
otro correo electrónico con el mismo nombre (la parte delante de la arroba @) pero con dominio 
lincolncollege.cl.
'''

initial_email = input('Ingrese un correo gmail:\n')
final_email = initial_email.replace('@gmail.com','@lincolncollege.cl')
print(final_email)

