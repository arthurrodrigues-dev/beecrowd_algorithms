T = int(input())
respostas = list(map(int, input().split()))

qtde = 0
for resposta in respostas:
  if resposta == T:
    qtde += 1

print(qtde)