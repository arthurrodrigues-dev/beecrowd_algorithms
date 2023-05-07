while True:
    try:
        m_velocidade_lesmas = []
        v_velocidade_lesmas = []

        num_lesmas = int(input())
        m_velocidade_lesmas.append(list(map(int, input().split())))

        for sublista in m_velocidade_lesmas:
            v_velocidade_lesmas.extend(sublista)
        
        def maior_nivel(vetor):
            maior_velocidade = 0
            for velocidade_lesma in vetor:
                if velocidade_lesma > maior_velocidade:
                    maior_velocidade = velocidade_lesma
                
            if maior_velocidade < 10:
                return 1
            elif maior_velocidade >= 10 and maior_velocidade < 20:
                return 2
            elif maior_velocidade >= 20:
                return 3

        
        print(maior_nivel(v_velocidade_lesmas))
    except EOFError:
        break