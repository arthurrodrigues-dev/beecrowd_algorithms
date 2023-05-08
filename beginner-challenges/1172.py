X = []
for i in range(10):
  valor = int(input())
  if (valor <= 0):
    X.append(1)
  else:
    X.append(valor)
  
for j in range(10):
  print("X[{}] = {}".format(j, X[j]))
