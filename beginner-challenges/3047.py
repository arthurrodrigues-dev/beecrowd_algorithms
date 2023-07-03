idade_monica = int(input())
filho_1 = int(input())
filho_2 = int(input())
filho_3 = idade_monica - (filho_1 + filho_2)

maior = [filho_1, filho_2, filho_3]

idade_maior = 0
for i in range(len(maior)):
    if maior[i] > idade_maior:
        idade_maior = maior[i]

print(idade_maior)

