positivos = soma = media = 0

for i in range(6):
  valor = float(input())
  if valor > 0:
    positivos += 1
    soma += valor

media = soma / positivos
print(positivos, "valores positivos")
print("{:.1f}".format(media))
