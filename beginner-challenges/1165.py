n = int(input())

for i in range(1, n + 1):
  num = int(input())
  divisores = 0
  for j in range(1, num + 1):
    if (num % j == 0):
      divisores += 1
  if (divisores == 2):
    print(num, "eh primo")
  else:
    print(num, "nao eh primo")
