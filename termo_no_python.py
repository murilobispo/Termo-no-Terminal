from random import choice

print('{:^26}'.format('\033[1mTERMO IN PYTHON\033[m'))

lista_palavras = []
with open("termo_palavras.txt") as arquivo:
    for filtro in arquivo:
        filtro = filtro.strip()
        lista_palavras.append(filtro)
palavra = choice(lista_palavras).upper()

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
            resultado = ["_" for letra in palavra]
            for x in range(0, len(cadeia)):
                if chute[x] == palavra[x]:
                    resultado[x] = '\033[1;42m{}\033[m'.format(chute[x])
                elif chute[x] in palavra:
                    resultado[x] = '\033[1;43m{}\033[m'.format(chute[x])
                else:
                    resultado[x] = '\033[1;40m{}\033[m'.format(chute[x])

            resultado = ''.join(resultado)
            lista_cadeia[abs(tentativas - 5)] = resultado

            if tentativas == 0:
                confirma_perdeu = True

if ganhou:
    print('\n{:^30}'.format('\033[1;46mGANHOU!\033[m'))
if perdeu:
    print('\n\033[1;46m palavra certa: {}\033[m'.format(palavra))
