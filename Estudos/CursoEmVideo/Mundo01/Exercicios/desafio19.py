# Um professor quer sortear um dos seus quatros alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome do escolhido

# A função coice(x) retorna um elemento aleatório da sequência não vazia x. 
# x é uma lista. Se x estiver vazio, levanta IndexError.

# import random
from random import choice
num1 = str(input('Qual o nome do aluno1: '))
num2 = str(input('Qual o nome do aluno2: '))
num3 = str(input('Qual o nome do aluno3: '))
num4 = str(input('Qual o nome do aluno4: '))

alunos = [num1, num2, num3, num4]
escolhido = choice(alunos)

print('\nO Aluno escolhido foi: {}'.format(escolhido))
