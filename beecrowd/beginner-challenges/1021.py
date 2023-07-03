N = float(input())
notas = [100, 50, 20, 10, 5, 2]
centavos = N * 100

print("NOTAS:")
for nota in notas:
  res = centavos // (nota * 100)
  print("{:.0f} nota(s) de R$ {}.00".format(res, nota))
  centavos %= (nota * 100)

moedas = [100, 50, 25, 10, 5, 1]

print("MOEDAS:")
for moeda in moedas:
  print("{} moeda(s) de R$ {:.2f}".format(int(centavos // moeda), moeda / 100))
  centavos = centavos % moeda
