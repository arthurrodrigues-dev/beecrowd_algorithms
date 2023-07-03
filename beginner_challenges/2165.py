def contando_caracteres(tweet):
    soma = 0
    for i in tweet:
        soma += 1
    return soma

tweet = input()
qtde_caracteres = contando_caracteres(tweet)

print("TWEET") if qtde_caracteres <= 140 else print("MUTE")