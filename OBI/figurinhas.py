n, c, m = map(int, input().split())
carimbadas = set(map(int, input().split()))
compradas = set(map(int, input().split()))

c -= len(carimbadas.intersection(compradas))

print(c)