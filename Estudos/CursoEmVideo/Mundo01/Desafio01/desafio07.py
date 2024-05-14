#07-Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
nota1 = float(input('Qual sua primeira nota: '))
nota2 = float(input('Qual sua segunda nota: '))
media = (nota1 + nota2)/2
print('A média entre {} e {} é: {:.1f}'.format(nota1, nota2, media))
