vetor = []

N = input()
vetor = list(map(int, input().split()))

def calcular_fatorial(num):
    fatorial = 1
    for i in range(1, num + 1):
        fatorial *= i
    return fatorial

for i in range(len(vetor)):
    divisores = 0
    for j in range(1, vetor[i] + 1):
        if vetor[i] % j == 0:
            divisores += 1
    if divisores == 2:
        print(f'{vetor[i]}! = {calcular_fatorial(vetor[i])}')
