from time import sleep
print('-' * 30)
print(f'{'PAR OU ÍMPAR':^30}')
print('-' * 30)
num = int(input('Em qual número você pensou? '))
print('Verificando...')
sleep(1.5)
if num % 2 == 0:
    print(f'\033[31mO número {num} que você pensou é PAR!\033[m')
else:
    print(f'\033[32mO número {num} que você pensou é ÍMPAR!\033[m')
print('Muito obrigado, volte sempre!')
