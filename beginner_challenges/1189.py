matriz = []
vetor = []

escolha = input()

for l in range(12):
    for c in range(12):
        numeros = float(input())
        vetor.append(numeros)
    matriz.append(vetor)
    vetor = []

cont = 0
soma = 0
for l in range(12):
    for c in range(12):
        if l > c and l < len(matriz) - c - 1:
           soma += matriz[l][c]
           cont += 1

media = soma / cont

if escolha == 'S':
    print('{:.1f}'.format(soma))
elif escolha == 'M':
    print('{:.1f}'.format(media))