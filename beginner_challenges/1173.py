n = []
num = int(input())
n.append(num)
print("N[{}] = {}".format(0, num))

for i in range(1, 10):
  n.append(n[i - 1] * 2)
  print("N[{}] = {}".format(i, n[i]))

