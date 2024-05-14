#06-Crie um algoritmo que leia um número e mostre o seu dobro, tripo e raiz quadrada.
numero = int(input('Digite um número: '))
print('Seu dobro é {}'.format(numero*2))
print('Seu triplo é {}'.format(numero*3))
print('Sua raiz quadrada é {:.2f}'.format(pow(numero,(1/2))))
