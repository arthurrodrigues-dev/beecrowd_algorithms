A = []

for i in range(100):
  valor = float(input())
  A.append(valor)

for j in range(100):
  if (A[j] <= 10):
    print("A[{}] = {}".format(j, A[j]))
