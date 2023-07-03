x = int(input())
while x != 0:
  output = []
  for i in range(1, x + 1):
    output.append(str(i))
  print(" ".join(output))
  x = int(input())
  
