'''
7.	Cree un programa que pregunte por los productos de una cesta de la compra, separados por comas, 
y muestre por pantalla cada uno de los productos en una línea distinta.
'''

shopping_cart = input('Ingrese la lista de productos que comprará, separando los elementos por comas: ')
final_shopping_cart = shopping_cart.replace(',','\n')
print(final_shopping_cart)