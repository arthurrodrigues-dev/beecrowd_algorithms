import string

alfabeto = list(string.ascii_uppercase)

N = int(input())
for i in range(N):
    my_string = input()
    num_deslocamento = int(input())

    my_string_array = []
    for letra in my_string:
        my_string_array.append(letra)

    index_correto = 0
    for j in range(len(my_string_array)):
        index_correto = alfabeto.index(my_string_array[j]) - num_deslocamento
        my_string_array[j] = alfabeto[index_correto]
        
    string_decodificada = ''.join(my_string_array)
    print(string_decodificada)

