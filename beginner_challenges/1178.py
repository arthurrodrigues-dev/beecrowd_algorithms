N = []
X = float(input())
N.append(X)

for i in range(1, 100):
  X /= 2
  N.append(X)

for j in range(0, 100):
  print('N[{}] = {:.4f}'.format(j, N[j]))
