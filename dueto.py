import funcoes

def dueto():
    funcoes.limpar()

    palavras = funcoes.gera_palavra(2)
    palavra1 = palavras[0]
    palavra2 = palavras[1]

    tentativas = 7
    erro = ''
    
    cadeia = '_' * len(palavra1)
    lista_cadeia1 = [cadeia for _ in range(0, tentativas)]
    lista_cadeia2 = [cadeia for _ in range(0, tentativas)]

    ganhou = False
    perdeu = False
    acertou1 = False
    acertou2 = False
    confirma_ganhou = False
    confirma_perdeu = False

    while not ganhou and not perdeu:
        funcoes.limpar()
        
        print('{:^39}\n'.format('\033[1mDUETO\033[m'))
        print('{:^39}'.format(erro))

        for i in range (0, len(lista_cadeia1)):
            print('       {}'.format(str(lista_cadeia1[i])), end='')
            print('       {}'.format(str(lista_cadeia2[i])))

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

        if chute == palavra1 and not acertou1:
            lista_cadeia1[abs(tentativas - 6)] = '\033[1;42m{}\033[m'.format(chute)
            acertou1 = True
        if chute == palavra2 and not acertou2:
            lista_cadeia2[abs(tentativas - 6)] = '\033[1;42m{}\033[m'.format(chute)
            acertou2 = True
        if acertou1 and acertou2:
            confirma_ganhou = True

        else:
            
            if not acertou1:
                lista_cadeia1[abs(tentativas - 6)] = funcoes.processa_chute(chute, palavra1)
            if not acertou2:
                lista_cadeia2[abs(tentativas - 6)] = funcoes.processa_chute(chute, palavra2)
            if tentativas == 0:
                confirma_perdeu = True

    if ganhou:
        print('\n{:^41}'.format('\033[1;46mGANHOU!\033[m'))
    if perdeu:
        print('\n\033[1;46mPalavras: {}, {}\033[m'.format(palavra1, palavra2))
    input("\nPressione ENTER para voltar ao menu")
