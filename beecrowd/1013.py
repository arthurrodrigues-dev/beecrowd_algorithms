a, b , c = input().split()
a, b, c = int(a), int(b), int(c)

maiorAB = (a + b + abs(a - b)) / 2
maiorAB = int(maiorAB)

if (c > maiorAB):
  print(c, "eh o maior")
else:
  print(maiorAB, "eh o maior")
