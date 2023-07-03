from collections import Counter

N = int(input())
valores = input().split()
for i in range(N):
    valores[i] = int(valores[i])

multiplos = [2, 3, 4, 5]
contador = Counter()

for valor in valores:
    for multiplo in multiplos:
        if valor % multiplo == 0:
            contador[multiplo] += 1
        else:
            contador[multiplo] += 0

for multiplo in multiplos:
    print(contador[multiplo], 'Multiplo(s) de', multiplo)