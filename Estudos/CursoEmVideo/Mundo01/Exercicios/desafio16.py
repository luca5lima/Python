# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.
# Ex: Digite um número: 6.127
# O número 6.127 tem a parte inteira 6.

# numero = float(input('Digite um número: '))
# print('O valor digitado foi {} e a sua porção inteira é {}'.format(numero, int(numero)))

# import math
from math import trunc
numero = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(numero, math.trunc(numero)))