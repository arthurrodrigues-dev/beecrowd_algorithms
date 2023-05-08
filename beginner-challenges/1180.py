posicao = menor = 0
n = int(input())

valores = input().split()
X = list(map(int, valores))

for i in range(n):
  if (i == 0):
    menor = X[i]
  if (X[i] < menor):
    menor = X[i]
    posicao = i

print("Menor valor: {}".format(menor))
print("Posicao: {}".format(posicao))
