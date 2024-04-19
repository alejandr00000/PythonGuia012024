'''
5.	Los números de teléfono en Chile tienen el prefijo +56 (por ejemplo +5612345678). Escriba un programa 
que pregunte por un número de teléfono con este formato y muestre en pantalla el mismo número, pero sin la 
extensión (en el ejemplo, 12345678).
'''

phone_number = input('Ingrese un número incluyendo el prefijo del país: ')

final_number01 = phone_number.replace('+56','')
print(final_number01)

#En la guía me equivoqué. Coloqué un ejemplo con ocho cifras. Los números de teléfono tienen 9
final_number02 = phone_number[-9:]
print(final_number02)
