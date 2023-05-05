from random import choice
from time import sleep
import os

def gera_palavra(quantidade_palavras):

    lista_palavras = []
    palavras = []
    with open("palavras.txt") as arquivo:
        for filtro in arquivo:
            filtro = filtro.strip()
            lista_palavras.append(filtro)
    while quantidade_palavras != 0:

        nova_palavra = choice(lista_palavras).upper()                       
        if nova_palavra not in palavras:
            palavras.append(nova_palavra)
            quantidade_palavras -= 1

    return palavras


def limpar():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

def recebe_chute():
    while True:
        chute = input('{:>7}'.format('>')).strip().upper()
        chute = chute.upper()
        chute = list(chute)

        letras_a_fora = ['Â', 'Ã', 'Á', 'À']
        letras_e_fora = ['É', 'È']


        for x in range(0, len(chute)):
            if chute[x] in letras_a_fora:
                chute[x] = 'A'
            if chute[x] in letras_e_fora:
                chute[x] = 'E'
            if chute[x] == 'Ç':
                chute[x] = 'C'

        chute = ''.join(chute)

        if len(chute) != 5:
            print('Fora do número de letras!!!')
            continue

        if not chute.isalpha():
            print('Somente letras!!!')
            continue

        return chute

def comecar():
    print('Começando em ')
    sleep(1)
    print('\033[1;40m{}\033[m'.format('3'))
    sleep(1)
    print('\033[1;43m{}\033[m'.format('2'))
    sleep(1)
    print('\033[1;42m{}\033[m'.format('1'))
    sleep(1)
