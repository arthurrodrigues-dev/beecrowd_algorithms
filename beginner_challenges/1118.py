def media():
  nota_valida = soma = 0
  
  while nota_valida != 2:
    nota = float(input())
    if nota >= 0 and nota <= 10:
      nota_valida += 1
      soma += nota
    else:
      print("nota invalida")
  
  print("media = {:.2f}".format(soma / nota_valida))

def novo_calculo():  
  res = 0
  while res != 1 and res != 2:
    print('novo calculo (1-sim 2-nao)')
    res = int(input())
    if res == 1 or res == 2:
      return res

media()
nc = novo_calculo()
while True:
  if nc == 1:
    media()
    nc = novo_calculo()
  elif nc == 2:
    break
