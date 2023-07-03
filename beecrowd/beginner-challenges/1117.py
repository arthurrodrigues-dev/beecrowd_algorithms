nota_valida = soma = 0

while nota_valida != 2:
  nota = float(input())
  if nota >= 0 and nota <= 10:
    nota_valida += 1
    soma += nota
  else:
    print("nota invalida")

print("media = {:.2f}".format(soma / nota_valida))

