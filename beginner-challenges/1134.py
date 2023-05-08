alcool = gasolina = diesel = 0

while True:
    cod = int(input())
    if (cod == 1):
        alcool = alcool + 1
    elif (cod == 2):
        gasolina = gasolina + 1
    elif (cod == 3):
        diesel = diesel + 1
    elif (cod == 4):
        break
  
print("MUITO OBRIGADO")
print("Alcool:", alcool)
print("Gasolina:", gasolina)
print("Diesel:", diesel)
    
        
