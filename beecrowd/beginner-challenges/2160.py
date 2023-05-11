def contando_caracteres(string):
    soma = 0
    for i in string:
        soma += 1
    return soma 


qtde_caracteres = contando_caracteres(input())

print("YES") if qtde_caracteres <= 80 else print("NO")