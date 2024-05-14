#11-Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la. 
#Sabendo que cada litro de tinta, pinta uma área de 2m².
largura = float(input('Digite a largura: '))
altura = float(input('Digite a altura: '))

area = largura * altura
litro = area / 2

print('{} litros de tinta pinta {} de area'.format(litro, area))
