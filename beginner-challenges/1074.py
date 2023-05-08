n = int(input())
for i in range(n):
  valor = int(input())
  
  if (valor == 0):
    print("NULL")
  elif (valor > 0) and (valor % 2 == 0):
    print("EVEN POSITIVE")
  elif (valor > 0) and (valor % 2 != 0):
    print("ODD POSITIVE")
  elif (valor < 0) and (valor % 2 == 0):
    print("EVEN NEGATIVE")
  else:
    print("ODD NEGATIVE")
