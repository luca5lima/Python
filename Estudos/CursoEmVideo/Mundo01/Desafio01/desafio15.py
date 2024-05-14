# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
dias = int(input('Quantos dias foi alugado: '))
km = float(input('Quantos Km foram percorridos: '))
preco_dias = dias * 60
precoKm = km * 0.15
preco_total = precoKm + preco_dias
print('Valor do aluguel é R${:.2f}'.format(preco_total))