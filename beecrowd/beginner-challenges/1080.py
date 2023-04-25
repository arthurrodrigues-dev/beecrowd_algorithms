maior = posicao_maior = num = 0

for i in range(1, 101):
    num = int(input()) 
    if (num > maior):
        maior = num
        posicao_maior = i
        
print(maior)
print(posicao_maior)
   

   
