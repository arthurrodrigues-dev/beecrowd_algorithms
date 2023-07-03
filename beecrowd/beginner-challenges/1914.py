QT = int(input())

for i in range(QT):
    jogador1, escolha1, jogador2, escolha2 = map(str, input().split())
    N, M = map(int, input().split())

    if (N + M) % 2 == 0 and escolha1 == 'PAR':
        print(jogador1)
    elif (N + M) % 2 == 0 and escolha2 == 'PAR':
        print(jogador2)
    elif (N + M) % 2 == 1 and escolha1 == 'IMPAR':
        print(jogador1)
    else:
        print(jogador2)


