# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

# As funções sin(x), cos(x), tan(x) / resuta respequitivamente seno, cosseno e tangente
# A função radians(x) convete o ângulo de graus para radianos

# import math
from math import sin, cos, tan, radians
angulo = float(input('Digite um ângulo: '))
angulo_r = radians(angulo)
print('Seu seno é: {:.2f} em radianos'.format(sin(angulo_r)))
print('Seu cosseno é: {:.2f} em radianos'.format(cos(angulo_r)))
print('Seu tangente é: {:.2f} em radianos'.format(tan(angulo_r)))
