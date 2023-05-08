import funcoes

def quarteto():
    funcoes.limpar()

    palavras = funcoes.gera_palavra(4)
    palavra1 = palavras[0]
    palavra2 = palavras[1]
    palavra3 = palavras[2]
    palavra4 = palavras[3]

    tentativas = 9
    erro = ''

    cadeia = '_' * len(palavra1)
    lista_cadeia1 = [cadeia for _ in range(0, tentativas)]
    lista_cadeia2 = [cadeia for _ in range(0, tentativas)]
    lista_cadeia3 = [cadeia for _ in range(0, tentativas)]
    lista_cadeia4 = [cadeia for _ in range(0, tentativas)]

    ganhou = False
    perdeu = False
    acertou1 = False
    acertou2 = False
    acertou3 = False
    acertou4 = False
    confirma_ganhou = False
    confirma_perdeu = False

    while not ganhou and not perdeu:
        funcoes.limpar()
        
        print('{:^62}\n'.format('\033[1mQUARTETO\033[m'))
        print('{:^62}'.format(erro))

        for i in range (0, len(lista_cadeia1)):
            print('       {}'.format(str(lista_cadeia1[i])), end='')
            print('       {}'.format(str(lista_cadeia2[i])), end='')
            print('       {}'.format(str(lista_cadeia3[i])), end='')
            print('       {}'.format(str(lista_cadeia4[i])))

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
            lista_cadeia1[abs(tentativas - 8)] = '\033[1;42m{}\033[m'.format(chute)
            acertou1 = True
        if chute == palavra2 and not acertou2:
            lista_cadeia2[abs(tentativas - 8)] = '\033[1;42m{}\033[m'.format(chute)
            acertou2 = True
        if chute == palavra3 and not acertou3:
            lista_cadeia3[abs(tentativas - 8)] = '\033[1;42m{}\033[m'.format(chute)
            acertou3 = True
        if chute == palavra4 and not acertou4:
            lista_cadeia4[abs(tentativas - 8)] = '\033[1;42m{}\033[m'.format(chute)
            acertou4 = True
        if acertou1 and acertou2 and acertou3 and acertou4:
            confirma_ganhou = True

        else:

            if not acertou1:
                lista_cadeia1[abs(tentativas - 8)] = funcoes.processa_chute(chute, palavra1)
            if not acertou2:
                lista_cadeia2[abs(tentativas - 8)] = funcoes.processa_chute(chute, palavra2)
            if not acertou3:
                lista_cadeia3[abs(tentativas - 8)] = funcoes.processa_chute(chute, palavra3)
            if not acertou4:
                lista_cadeia4[abs(tentativas - 8)] = funcoes.processa_chute(chute, palavra4)

            if tentativas == 0:
                confirma_perdeu = True

    if ganhou:
        print('\n{:^65}'.format('\033[1;46mGANHOU!\033[m'))
    if perdeu:
        print('\n\033[1;46mPalavras: {}, {}, {}, {}\033[m'.format(palavra1, palavra2, palavra3, palavra4))
    input("\nPressione ENTER para voltar ao menu")