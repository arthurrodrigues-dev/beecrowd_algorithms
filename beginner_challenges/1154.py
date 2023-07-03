qtde_idades = soma_idades = 0
idade = int(input())

while (idade > 0):
  qtde_idades += 1
  soma_idades += idade
  idade = int(input())

media_idades = soma_idades / qtde_idades
print("{:.2f}".format(media_idades))
