dicionario = {
    1001: 1.5,
    1002: 2.5,
    1003: 3.5,
    1004: 4.5,
    1005: 5.5
}

def calcula(code, qtd):
    return dicionario[code] * qtd

soma = 0
produtos_comprados = int(input())
for i in range(produtos_comprados):
    codigo, qtde = map(int, input().split())
    soma += calcula(codigo, qtde)

print('{:.2f}'.format(soma))
