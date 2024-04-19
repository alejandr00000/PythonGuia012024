'''
13.	Cree un programa que permita calcular la distancia entre dos puntos del plano cartesiano.
'''

punto_Ax = float(input('Ingrese la coordenada x del punto A:' ))
punto_Ay = float(input('Ingrese la coordenada y del punto A:' ))

punto_Bx = float(input('Ingrese la coordenada x del punto B:' ))
punto_By = float(input('Ingrese la coordenada y del punto B:' ))

distancia = ((punto_Ax-punto_Bx)**2 + (punto_Ay - punto_By)**2)**1/2

mensaje = f'La distancia entre el punto A({punto_Ax},{punto_Ay}) y el punto B({punto_Bx},{punto_By}) es {distancia}'

print(mensaje)