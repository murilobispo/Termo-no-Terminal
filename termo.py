import funcoes

def termo():

    funcoes.limpar()
    palavras = funcoes.gera_palavra(1)
    palavra = palavras[0]
    cadeia = '_' * len(palavra)
    lista_cadeia = [cadeia for _ in range(0, 6)]

    ganhou = False
    perdeu = False
    confirma_ganhou = False
    confirma_perdeu = False
    tentativas = 6

    while not ganhou and not perdeu:

        funcoes.limpar()
        print('{:^26}'.format('\033[1mTERMO\033[m'))
        print('\n')
        for cadeias in lista_cadeia:
            print('       {}'.format(str(cadeias)))

        if confirma_ganhou:
            ganhou = True
            break
        elif confirma_perdeu:
            perdeu = True
            break

        chute = funcoes.recebe_chute()

        tentativas -= 1

        if chute == palavra:
            lista_cadeia[abs(tentativas - 5)] = '\033[1;42m{}\033[m'.format(chute)
            confirma_ganhou = True

        else:
            indice_letras_erradas   = []
            resultado = ["_" for letra in palavra]

            for x in range(0, len(cadeia)):
                indice_letras_erradas.append(x)
                resultado[x] = '\033[1;40m{}\033[m'.format(chute[x])

                if chute[x] == palavra[x]:
                    resultado[x] = '\033[1;42m{}\033[m'.format(chute[x])
                    indice_letras_erradas.remove(x)
            
            letras_restantes = []
            for i in indice_letras_erradas  :
                letras_restantes.append(palavra[i])

            for i in indice_letras_erradas:
                if chute[i] in letras_restantes:
                    resultado[i] = '\033[1;43m{}\033[m'.format(chute[i])
                    letras_restantes.remove(chute[i])
        
            resultado = ''.join(resultado)
            lista_cadeia[abs(tentativas - 5)] = resultado

            if tentativas == 0:
                confirma_perdeu = True

    if ganhou:
        print('\n{:^30}'.format('\033[1;46mGANHOU!\033[m'))
    if perdeu:
        print('\n\033[1;46m palavra certa: {}\033[m'.format(palavra))
    input("\nPressione ENTER para voltar ao menu")
