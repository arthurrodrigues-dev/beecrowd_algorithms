i = 1
j = 7
for k in range(5):
  for l in range(3):
    print("I={} J={}".format(i, j))
    if (l == 2):
      j += 4
    else:
      j -= 1 
  i += 2
