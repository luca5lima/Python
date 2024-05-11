# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todos as informações possiveis sobre ele.
algo = input('Digite algo: ')
print('Seu tipo primitivo é {}'.format(type(algo)))
print('Só tem espaços: {}'.format(algo.isspace()))
print('Ele é um numero: {}'.format(algo.isnumeric()))
print('Ele é uma letra: {}'.format(algo.isalpha()))
print('Ele é alfanumerico: {}'.format(algo.isalnum()))
print('Está em maiúsculas: {}'.format(algo.isupper()))
print('Está em minúsculas: {}'.format(algo.islower()))
print('Está capitalizada: {}'.format(algo.istitle()))

# algo é um objeto, ele tem característicasd e realiza funcionsalidades, astibutos e metodos, tudo que tem parenteses no final representa metodos, todo objeto tem metodos 