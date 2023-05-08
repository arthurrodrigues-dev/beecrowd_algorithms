s = 1
d = 1
total = res = 0
for i in range(3, 22):
  d *= 2
  s += 2
  res = s / d
  total += res

print("{:.2f}".format(total + 1))
