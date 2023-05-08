from random import choice
from time import sleep
import os
from unidecode import unidecode

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

def recebe_chute(chute):
    chute = chute.strip().upper()
    chute = unidecode(chute)
    
    erro = ''

    if not chute.isalpha():
        erro = '\033[4mSomente letras!\033[m'
    elif len(chute) > 5:
        erro = '\033[4mMuito comprido!\033[m'
    elif len(chute) < 5:
        erro = '\033[4mMuito pequeno!\033[m'
    
    resultados = [chute, erro]
    return resultados

def comecar():
    print('Começando em ')
    sleep(1)
    print('\033[1;40m{}\033[m'.format('3'))
    sleep(1)
    print('\033[1;43m{}\033[m'.format('2'))
    sleep(1)
    print('\033[1;42m{}\033[m'.format('1'))
    sleep(1)

def processa_chute(chute, palavra):
    indice_letras_erradas   = []
    resultado = ["_" for letra in palavra]

    for x in range(0, 5):
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
    return resultado

def sobre():
    limpar()
    msg_sobre = '''Fiz esse programa que tenta replicar
o conhecido jogo da web "Termo", porém
apenas com o uso do terminal. Com o intuito 
de por em dia alguns de meus conhecimentos 
em Python.'''
    print(msg_sobre)
    input("\nPressione ENTER para voltar ao menu")