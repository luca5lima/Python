#08-Escreva um programa que leia um valor em metros e exiba convertido em centimetros e milimetros.
metro = float(input('Quantos metros: '))
cm = metro * 100
mm = metro * 1000
print('{}m é igual {}cm que é igual {:.0f}mm'.format(metro, cm, mm))
