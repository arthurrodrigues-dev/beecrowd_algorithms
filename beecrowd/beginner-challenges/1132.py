soma = 0
x, y = int(input()), int(input())

if (y < x):
  for i in range(y, x + 1):
    if (i % 13 != 0):
      soma += i
else:
  for i in range(x, y + 1):
    if (i % 13 != 0):
      soma += i

print(soma)
    
    
      
  
