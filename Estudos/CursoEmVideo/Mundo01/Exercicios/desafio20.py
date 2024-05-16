# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatros e mostre a ordem sorteada

# A função shuffle(x) Embaralha a sequência x internamente.
# x é uma lista

# import random
from random import shuffle
num1 = str(input('Qual o nome do aluno1: '))
num2 = str(input('Qual o nome do aluno2: '))
num3 = str(input('Qual o nome do aluno3: '))
num4 = str(input('Qual o nome do aluno4: '))

alunos = [num1, num2, num3, num4]
shuffle(alunos)

print('A nova ordem de apresentação será: \n{}'.format(alunos))