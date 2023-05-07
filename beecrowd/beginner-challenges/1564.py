while True:
    try:
        num_reclamacoes = int(input())
        if num_reclamacoes > 0:
            print('vai ter duas!')
        else:
            print('vai ter copa!')
    except EOFError:
        break