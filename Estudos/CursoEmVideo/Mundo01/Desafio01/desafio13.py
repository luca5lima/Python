#13-Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario = float(input('Qual o seu salario: R$'))
aumento = salario * 0.15 #15/100 == 0.15
salario_aumento = salario + aumento
print('O salario de R${:.2f} com aumento de 15% vai ser de R${:.2f}'.format(salario, salario_aumento))