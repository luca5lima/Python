#Escreva um programa que converta uma temperatura digitada em °C para °F
c = float(input('Digite a temperatura em °C: '))
f = ((9 * c) / 5) + 32
print('A temperatura de {}°C é igual a {}°F'.format(c, f))