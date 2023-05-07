C = int(input())

for i in range(C):
    nome, forca = map(str, input().split())
    forca = int(forca)
    if nome == 'Thor':
        print('Y')
    else:
        print('N')