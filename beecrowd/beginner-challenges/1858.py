N = int(input())
T = list(map(int, input().split()))

for i in range(len(T)):
    if i == 0:
        menor = T[i]
    if T[i] < menor:
        menor = T[i]
    
print(T.index(menor) + 1)