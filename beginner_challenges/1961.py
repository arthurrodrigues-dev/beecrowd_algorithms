altura_pulo_sapo, numero_canos = map(int, input().split())
alturas_canos = list(map(int, input().split()))

diff = []

for i in range(0, len(alturas_canos) - 1, 2):
    valor1 = alturas_canos[i]
    valor2 = alturas_canos[i + 1]

    diferenca = 0
    if valor1 < valor2:
        diferenca = valor2 - valor1
    else:
        diferenca = valor1 - valor2
    diff.append(diferenca) 

game_over = False

for altura in diff:
    if altura <= altura_pulo_sapo:
        continue
    else:
        game_over = True
        break

print("GAME OVER") if game_over else print("YOU WIN")