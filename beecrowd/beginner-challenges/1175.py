N = []

for i in range(20):
  array_values = int(input())
  N.append(array_values)
length = len(N)
  
for i in range(length // 2):
  N[i], N[length - i - 1] = N[length - i - 1], N[i]

for i in range(20):
  print("N[{}] = {}".format(i, N[i]))
