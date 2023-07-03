n = int(input())

for i in range(1, n + 1):
  num = int(input())
  soma_divisores = 0
  for j in range(1, num):
    if (num % j == 0):
      soma_divisores += j
  if (soma_divisores == num):
    print(num, "eh perfeito")
  else:
    print(num, "nao eh perfeito")
