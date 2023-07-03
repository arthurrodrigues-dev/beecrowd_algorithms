matriz = [[0] * 12 for i in range(12)] 
O = input()

for l in range(len(matriz)):
    for c in range(len(matriz)):
        matriz[l][c] = float(input())

soma = 0
cont = 0
for l in range(len(matriz)):
    for c in range(len(matriz)):
        if l > c and l > len(matriz) - c - 1:
            soma += matriz[l][c]
            cont += 1

media = soma / cont

if O == 'S':
    print('{:.1f}'.format(soma))
elif O == 'M':
    print('{:.1f}'.format(media))