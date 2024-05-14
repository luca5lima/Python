d = int(input())
a = int(input())
n = int(input())

chegada = n

if chegada > 15:
    chegada = 15

diaria = d + ((chegada - 1) * a)

# n + dias == 32
quant_de_dias = 32 - n

valor = quant_de_dias * diaria

print(valor)
