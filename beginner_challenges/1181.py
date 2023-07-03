matriz = []
vetor = []

linha = int(input())
escolha = input()

for l in range(12):
    for c in range(12):
        numeros = float(input())
        vetor.append(numeros)
    matriz.append(vetor)
    vetor = []

soma = 0
for l in range(12):
    for c in range(12):
        if l == linha:
            soma += matriz[l][c]

media = soma / 12

if escolha == 'S':
    print('{:.1f}'.format(soma))
elif escolha == 'M':
    print('{:.1f}'.format(media))