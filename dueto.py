import funcoes

def dueto():
    funcoes.limpar()
    palavras = funcoes.gera_palavra(2)
    palavra1 = palavras[0]
    palavra2 = palavras[1]

    tentativas = 7
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
        print('{:^39}'.format('\033[1mDUETO\033[m'))
        print('\n')


        for i in range (0, len(lista_cadeia1)):
            print('       {}'.format(str(lista_cadeia1[i])), end='')
            print('       {}'.format(str(lista_cadeia2[i])))

        if confirma_ganhou:
            ganhou = True
            break
        elif confirma_perdeu:
            perdeu = True
            break

        chute = funcoes.recebe_chute()

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

                indice_letras_erradas   = []
                resultado = ["_" for letra in palavra1]
                for x in range(0, len(cadeia)):
                    indice_letras_erradas.append(x)
                    resultado[x] = '\033[1;40m{}\033[m'.format(chute[x])

                    if chute[x] == palavra1[x]:
                        resultado[x] = '\033[1;42m{}\033[m'.format(chute[x])
                        indice_letras_erradas.remove(x)
                
                letras_restantes = []
                for i in indice_letras_erradas  :
                    letras_restantes.append(palavra1[i])

                for i in indice_letras_erradas:
                    if chute[i] in letras_restantes:
                        resultado[i] = '\033[1;43m{}\033[m'.format(chute[i])
                        letras_restantes.remove(chute[i])
            
                resultado = ''.join(resultado)
                lista_cadeia1[abs(tentativas - 6)] = resultado

            ################################
            if not acertou2:

                indice_letras_erradas   = []
                resultado = ["_" for letra in palavra2]

                for x in range(0, len(cadeia)):
                    indice_letras_erradas.append(x)
                    resultado[x] = '\033[1;40m{}\033[m'.format(chute[x])

                    if chute[x] == palavra2[x]:
                        resultado[x] = '\033[1;42m{}\033[m'.format(chute[x])
                        indice_letras_erradas.remove(x)
                
                letras_restantes = []
                for i in indice_letras_erradas  :
                    letras_restantes.append(palavra2[i])

                for i in indice_letras_erradas:
                    if chute[i] in letras_restantes:
                        resultado[i] = '\033[1;43m{}\033[m'.format(chute[i])
                        letras_restantes.remove(chute[i])
            
                resultado = ''.join(resultado)
                lista_cadeia2[abs(tentativas - 6)] = resultado


            if tentativas == 0:
                confirma_perdeu = True

    if ganhou:
        print('\n{:^41}'.format('\033[1;46mGANHOU!\033[m'))
    if perdeu:
        print('\n\033[1;46mPalavras: {}, {}\033[m'.format(palavra1, palavra2))
    input("\nPressione ENTER para voltar ao menu")
