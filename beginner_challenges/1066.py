valor = pares = impares = positivos = negativos = 0
for i in range(5):
    valor = int(input())
    if (valor % 2 == 0):
        pares = pares + 1
    else:
        impares = impares + 1
    if (valor > 0):
        positivos = positivos + 1
    elif (valor < 0):
        negativos = negativos + 1

print(pares, "valor(es) par(es)")
print(impares, "valor(es) impar(es)")
print(positivos, "valor(es) positivo(s)")
print(negativos, "valor(es) negativo(s)")
    
    
