x, y = input().split()
x, y = int(x), int(y)

for i in range(1, y + 1):
  if (i == y):
    print(i)
  else:
    print(i, end=" ")
  if (i % x == 0):
    print()
  
