def mensagem(msg):
    from time import sleep
    tam = len(msg) + 10
    print('-' * tam)
    print(f'     {msg:^}')
    print('-' * tam)
    sleep(1)


mensagem('JOGO MAD LIBS')
cor = str(input('Digite uma cor no plural: ')).lower().strip()
substantivo_plural = str(input('Digite algum substantivo no plural: ')).lower().strip()
substantivo = str(input('Digite uma parte do corpo: ')).lower().strip()
mensagem('POEMA')
print(f'Rosas são {cor},')
print(f'{substantivo_plural} são azuis,')
print(f'Esse seu(a) {substantivo} é o que me seduz.')
