x, y = int(input()), int(input())

if (y > x):
  soma = 0
  for i in range(x + 1, y):
    if (i % 2 != 0):
      soma += i
  print(soma)
else:
  soma = 0
  for i in range(y + 1, x):
    if (i % 2 != 0):
      soma += i
  print(soma)
