# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um retângulo.
# Calcule e mostre o comprimento da hipotenusa.

# co = float(input('Comprimento do cateto oposto: '))
# ca = float(input('Comprimento do cateto adjacente: '))
# h = (co ** 2 + ca **2) ** (1/2)
# print('A hipotenusa vai medir {:.2f}'.format(h))

# import math
from math import hypot
oposto = float(input('Qual é o cateto oposto: '))
adjacente = float(input('Qual é o cateto adjacente: '))
hipotenusa = hypot(oposto, adjacente)
print('A hipotenusa vai medir: {:.2f}'.format(hipotenusa))

#https://docs.python.org/pt-br/3/library/math.html