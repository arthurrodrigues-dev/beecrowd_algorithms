T = int(input())
N = []

for i in range(1000):
  for j in range(T):
    N.append(j)


for k in range(1000):
  print("N[{}] = {}".format(k, N[k]))
