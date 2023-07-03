def str_para_binario(string):
  dic = {'*': '1', '-': '0'}

  str_array = list(string)
  num_binario = []
  
  for i in range(len(string)):
    if str_array[i] in dic:
      num_binario.append(dic[str_array[i]]) 

  decimal = binario_para_decimal(num_binario)
  return decimal

def binario_para_decimal(binario):
  dic = {0: '4', 1: '2', 2: '1'}
  
  decimal = 0
  for i in range(3):
    if binario[i] == '1':
      decimal += int(dic[i])

  return decimal
    
soma = num_gritos = 0

while num_gritos < 3:
  entrada = input()
  if entrada != 'caw caw':
    piscada = entrada
    num_decimal = str_para_binario(piscada)
    soma += num_decimal
  else:
    num_gritos += 1
    print(soma)
    soma = 0

