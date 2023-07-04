while True: 
    M, N = map(int, input().split())
    if M == 0 and N == 0 : break
    soma = str(M + N)

    vetor_string = [caractere for caractere in soma if caractere != '0']
    print("".join(vetor_string))
