L = int(input())
C = int(input())

matriz = []
vetor = []

for l in range(L):
    for c in range(C):
        if l % 2 == 0 and c % 2 != 0 or c % 2 == 0 and l % 2 != 0:
            vetor.append(0)
        else:
            vetor.append(1)
    matriz.append(vetor)
    vetor = []

print(matriz[L - 1][C - 1])