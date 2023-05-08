n1, n2, n3 = input().split()
n1, n2, n3 = int(n1), int(n2), int(n3)

maior = menor = meio = 0

if n1 > n2 and n1 > n3:
  maior = n1
  if (n2 > n3):
    meio = n2
    menor = n3
  else:
    meio = n3
    menor = n2
elif n2 > n1 and n2 > n3:
  maior = n2
  if (n1 > n3):
    meio = n1
    menor = n3
  else:
    meio = n3
    menor = n1
else:
  maior = n3
  if (n1 > n2):
    meio = n1
    menor = n2
  else:
    meio = n2
    menor = n1

print(menor, meio, maior, sep="\n")
print()
print(n1, n2, n3, sep="\n")
