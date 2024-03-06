from random import randint
from time import sleep

ganhou = perdeu = empate = 0
print('-' * 30)
print(f'{'J O G O  D A  V E L H A':^30}')
print('-' * 30)
while True:
    computador = ['Pedra', 'Papel', 'Tesoura']
    sort = randint(0, 2)
    jogador = int(input('Digite [1] para escolher Pedra, [2] para Papel e [3] para Tesoura: '))
    while jogador < 1 or jogador > 3:
        jogador = int(input('ERRO, Tente novamente! Escolha somente entre [1 / 2 / 3]: '))
    print(f'\033[35mO computador escolheu {computador[sort]}!\033[m')
    print(f'\033[36mE você escolheu {computador[jogador-1]}\033[m')
    if jogador == 1 and sort == 2:
        print('\033[32mVocê venceu, parabéns!\033[m')
        ganhou += 1
    elif jogador == 1 and sort == 1:
        print('\033[31mVocê perdeu... Tente novamente!\033[m')
        perdeu += 0
    elif jogador == 2 and sort == 0:
        print('\033[32mVocê venceu, parabéns!\033[m')
        ganhou += 1
    elif jogador == 2 and sort == 2:
        print('\033[31mVocê perdeu... Tente novamente!\033[m')
        perdeu += 1
    elif jogador == 3 and sort == 0:
        print('\033[31mVocê perdeu... Tente novamente!\033[m')
        perdeu += 1
    elif jogador == 3 and sort == 1:
        print('\033[32mVocê venceu, parabéns!\033[m')
        ganhou += 1
    elif (jogador - 1) == sort:
        print('\033[33mDeu empate... Tente novamente!\033[m')
        empate += 1
    resp = str(input('Deseja continuar jogando? [S/N] '))
    if resp in 'Nn':
        break
print('Calculando...')
sleep(1.5)
print('-' * 30)
print(f'{'P L A C A R':^30}')
print('-' * 30)
print(f'Você ganhou {ganhou} vezes!\nVocê perdeu {perdeu} vezes!\nE o jogo ficou empatado {empate} vezes!')
