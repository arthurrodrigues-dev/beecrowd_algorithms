n = int(input())

for i in range(n):
  x, y = input().split()
  x, y = int(x), int(y)

  if (y > x):
    soma = 0
    for j in range(x + 1, y):
      if (j % 2 != 0):
        soma += j
    print(soma)
  else:
    soma = 0
    for j in range(y + 1, x):
      if (j % 2 != 0):
        soma += j
    print(soma)


