N = int(input())

v1 = 0
v2 = 1
v3 = v2 + v1

numeros = [v1, v2, v3]
str_numeros = []

aux = 0
for i in range(N - 3):
  aux = v2
  v2 = v3
  v1 = aux
  v3 = v1 + v2 
  numeros.append(v3)

for numero in numeros:
  str_numeros.append(str(numero))

print(" ".join(str_numeros))
