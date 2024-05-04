n1=int(input('Digite o primeiro numero: '))
n2=int(input('Digite o segundo numero: '))
n3=int(input('Digite o terceiro numero: '))

if (n1 <= n2 and n2 <= n3):
    menor = n1
elif (n2 <= n1 and n2 <= n3):
    menor = n2
elif (n3 <= n1 and n3 <= n2):
    menor = n3

elif (n1 >= n2 and n2 >= n3):
    maior = n1
elif (n2 >= n1 and n2 >= n3):
    maior = n2
elif (n3 >= n1 and n3 >= n2):
    maior = n3

elif (n2 >= n1 and n2 <= n3):
    medio = int(n2)
elif (n1 >= n2 and n1 <= n3):
    medio = int(n1)
else:
    medio = int(n3)

print('Menor: ', menor,'Medio: ' ,medio,'Maior', maior)