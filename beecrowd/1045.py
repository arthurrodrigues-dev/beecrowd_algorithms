a, b, c = input().split()
a, b, c = float(a), float(b), float(c)

if (b > c) and (b > a):
  a, b = b, a
  if b < c:
    b, c = c, b
elif (c > a) and (c > b):
  a, c = c, a
  if c > b:
    b, c = c, b
elif (c > b):
    b, c = c, b
  
if (a >= b + c):
  print("NAO FORMA TRIANGULO")
else:
  if (a ** 2) == (b ** 2) + (c ** 2):
    print("TRIANGULO RETANGULO")
  if (a ** 2) > (b ** 2) + (c ** 2):
    print("TRIANGULO OBTUSANGULO")
  if (a ** 2) < (b ** 2) + (c ** 2):
    print("TRIANGULO ACUTANGULO")
  if a == b and b == c:
    print("TRIANGULO EQUILATERO")
  if (a == c) and (a != b) or (b == a) and (b != c) or (c == b) and (c != a):
    print("TRIANGULO ISOSCELES")
