from termo import termo
from dueto    import dueto
from quarteto import quarteto
import funcoes
print('{:^26}'.format('\033[1mTERMO EM PYTHON\033[m'))

fim = False

while not fim:

    print('\n{}'.format('Escolha a modo:'))
    print('{}'.format('\033[1m[1]\033[m Termo'))
    print('{}'.format('\033[1m[2]\033[m Dueto'))
    print('{}'.format('\033[1m[3]\033[m Quarteto'))
    print('{}'.format('\033[1m[4]\033[m Sair'))

    escolha = input('{}'.format('>')).strip().upper()

    if escolha == '1':
        funcoes.comecar()
        termo()
    elif escolha == '2':
        funcoes.comecar()
        dueto()
    elif escolha == '3':
        funcoes.comecar()
        quarteto()
    elif escolha == '4':
        fim = True
    funcoes.limpar()

print('Obrigado por jogar, link do repositório: github.com/murilobispo/Termo-em-Python\n')
