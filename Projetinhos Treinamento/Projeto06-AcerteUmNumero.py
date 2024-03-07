from random import randint
from time import sleep
errou = 0
print('-' * 40)
print(f'{'\033[35mACERTE O NÚMERO SORTEADO\033[m':^48}')
print('-' * 40)
while True:
    sort = randint(1, 50)
    usuario = int(input('Digite um número entre 1 e 50: '))
    while usuario > 50 or usuario < 1:
        usuario = int(input('ERRO! Tente apenas números entre 1 e 50: '))
    print(f'\033[34mO computador sorteou o número {sort}!\033[m')
    if usuario == sort:
        print('\033[32mParabéns!!! Você acertou!\033[m')
        acertou = True
        break
    elif usuario != sort:
        print('\033[31mInfelizmente você não acertou... Tente novamente!\033[m')
        errou += 1
    resp = str(input('Deseja continuar? [S/N] '))
    if resp in 'Nn':
        break
print('Calculando partidas...')
sleep(1.5)
if acertou: 
    print(f'\033[32mVocê precisou de {errou} tentativas até acertar!\033[m')
elif not acertou:
    print(f'\033[31mVocê tentou {errou} vezes e infelizmente não acertou...\033[m')
