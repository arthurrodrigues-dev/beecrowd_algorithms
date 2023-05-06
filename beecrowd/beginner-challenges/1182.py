matriz = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

C = int(input())
resp = input()

if resp == 'S':
    for l in range(12):
        for c in range(12):
            matriz[l][c] = float(input())

    soma = 0
    for l in range(12):
        for c in range(12):
            if c == C:
                soma += matriz[l][c]
    print(soma)
elif resp == 'M':
    for l in range(12):
        for c in range(12):
            matriz[l][c] = float(input())

    soma = 0
    for l in range(12):
        for c in range(12):
            if c == C:
                soma += matriz[l][c]
    media = soma / 12
    print('{:.1f}'.format(media))