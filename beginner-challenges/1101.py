while True:
  m, n = input().split()
  m, n = int(m), int(n)
  if (m <= 0) or (n <= 0):
    break
  elif (m > n):
    soma = 0
    for i in range(n, m + 1):
      soma += i
      print(i, end=" ")
    print("Sum={}".format(soma))
  else:
    soma = 0
    for i in range(m, n + 1):
      soma += i
      print(i, end=" ")
    print("Sum={}".format(soma))
        
