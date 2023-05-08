# 3. Escreva um programa para ler 6 números. Após a leitura dos números, verifique,
# para cada um deles, se é distinto, ou seja, não possui repetição.

vetor = [0] * 6

for i in range(len(vetor)):
    vetor[i] = float(input())

tem_repeticao = False
for i in range(len(vetor)):
    for j in range(i + 1, len(vetor)):
        if vetor[i] == vetor[j]:
            tem_repeticao = True
            break
    if tem_repeticao:
        break

if tem_repeticao:
    print('O vetor possui elementos repetidos')
else:
    print('O vetor não possui elementos repeitidos')