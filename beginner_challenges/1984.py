numero = int(input())
vetor = []

for digito in str(numero):
    vetor.append(digito)

vetor.reverse()
numero = ''.join(vetor)
print(numero)
