from random import choice

print('{:^26}'.format('\033[1mTERMO IN PYTHON\033[m'))

lista_palavras = []
with open("termo_palavras.txt") as arquivo:
    for filtro in arquivo:
        filtro = filtro.strip()
        lista_palavras.append(filtro)
palavra = choice(lista_palavras).upper()
palavra = 'cabra'.upper()

cadeia = '_' * len(palavra)
lista_cadeia = [cadeia for _ in range(0, 6)]

ganhou = False
perdeu = False
confirma_ganhou = False
confirma_perdeu = False
tentativas = 6

while not ganhou and not perdeu:

    for cadeias in lista_cadeia:
        print('       {}'.format(str(cadeias)))

    if confirma_ganhou:
        ganhou = True
        break
    elif confirma_perdeu:
        perdeu = True
        break

    chute = str(input('{:>7}'.format('>'))).strip().upper()
    print('')

    if len(chute) != len(palavra):
        print('Fora do número de letras!!!')
        continue
    if not chute.isalpha():
        print('Somente letras!!!')
        continue
    else:
        tentativas -= 1
        if chute == palavra:
            lista_cadeia[abs(tentativas - 5)] = '\033[1;42m{}\033[m'.format(chute)
            confirma_ganhou = True
        else:
            #letras_2fa       = []
            letras_acertadas = []
            letras_erradas   = []
            resultado = ["_" for letra in palavra]

            for x in range(0, len(cadeia)):
                #letras_2fa.append(chute[x])
                letras_erradas.append(chute[x])
                resultado[x] = '\033[1;40m{}\033[m'.format(chute[x])

                if chute[x] == palavra[x]:
                    resultado[x] = '\033[1;37;42m{}\033[m'.format(chute[x])
                    #letras_2fa.remove(palavra[x])
                    letras_acertadas.append(palavra[x])
                    letras_erradas.remove(palavra[x])
            
            #while len(letras_2fa) != 0:
            print(letras_acertadas)
            print(letras_erradas)


            for i in letras_erradas:
                if i in palavra:
                    print(i)

            
            #for i in range(0, len(letras_2fa)):
                #letra_verificar = letras_2fa[i]
                #indexes = [i for i, c in enumerate(palavra) if c == letra_verificar]

                #for l in range(0, len(indexes)):
                    #print(indexes[l])

                #if letras_2fa[i] in palavra :
                    #print(i)
                    #print(letras_2fa[i])



            #resultado[x] = '\033[1;43m{}\033[m'.format(chute[x])
            #print(letras_2fa)
            #print(palavra)
            #letras_2fa.pop(0)


            
            resultado = ''.join(resultado)
            lista_cadeia[abs(tentativas - 5)] = resultado

            if tentativas == 0:
                confirma_perdeu = True

if ganhou:
    print('\n{:^30}'.format('\033[1;46mGANHOU!\033[m'))
if perdeu:
    print('\n\033[1;46m palavra certa: {}\033[m'.format(palavra))
