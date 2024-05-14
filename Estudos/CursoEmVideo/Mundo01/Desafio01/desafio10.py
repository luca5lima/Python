#10-Crie um programa que leia quanto dinheiro tem na carteira e mostre quantos Dólares ela pode comprar.
#Considere: US$1.00 = R$3.27
dinheiro = float(input('Quanto você tem em Reais? R$'))
dolar = dinheiro / 3.27
print ('Com R${:.2f} você pode comprar US${:.2f}'.format(dinheiro, dolar))
