#12-Faça um algoritmo que leia o preço de um produto e mostre seu novo preço,com 5% de desconto.
produto = float(input('Digite o valor do produto: R$'))
desconto = produto * (5/100) #5% == (5/100)
novo = produto - desconto
print('O produto que custa R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}'.format(produto, novo))
