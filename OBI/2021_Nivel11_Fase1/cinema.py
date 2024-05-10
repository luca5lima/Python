idadeA = int(input())
idadeB = int(input())

soma = 0
if (idadeA <= 17):
    soma += 15
elif (idadeA >= 18 and idadeA <= 59):
    soma += 30
else:
    soma += 20

if (idadeB <= 17):
    soma += 15
elif (idadeB >= 18 and idadeB <= 59):
    soma += 30
else:
    soma += 20

print(soma)