import funcoes

def termo():
    funcoes.limpar()

    palavras = funcoes.gera_palavra(1)
    palavra = palavras[0]

    tentativas = 6
    erro = ''

    cadeia = '_' * len(palavra)
    lista_cadeia = [cadeia for _ in range(0, tentativas)]

    ganhou = False
    perdeu = False
    confirma_ganhou = False
    confirma_perdeu = False

    while not ganhou and not perdeu:
        funcoes.limpar()

        print('{:^26}\n'.format('\033[1mTERMO\033[m'))
        print('{:^28}'.format(erro))

        for cadeias in lista_cadeia:
            print('       {}'.format(str(cadeias)))
            
        if confirma_ganhou:
            ganhou = True
            break
        elif confirma_perdeu:
            perdeu = True
            break

        chute = input('{:>7}'.format('>'))
        resultados = funcoes.recebe_chute(chute)
        chute = resultados[0]
        erro  = resultados[1]
        if erro:
            continue 

        tentativas -= 1

        if chute == palavra:
            lista_cadeia[abs(tentativas - 5)] = '\033[1;42m{}\033[m'.format(chute)
            confirma_ganhou = True

        else:
            lista_cadeia[abs(tentativas - 5)] = funcoes.processa_chute(chute, palavra)

            if tentativas == 0:
                confirma_perdeu = True

    if ganhou:
        print('\n{:^30}'.format('\033[1;46mGANHOU!\033[m'))
    if perdeu:
        print('\n\033[1;46mPalavra: {}\033[m'.format(palavra))
    input("\nPressione ENTER para voltar ao menu")
