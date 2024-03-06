def painel(msg):
    print('-' * 40)
    print(f'{msg:^40}')
    print('-' * 40)


painel('INFORMAÇÕES BIBLÍOGRÁFICAS')
nome = str(input('Qual é o seu nome? '))
while '*' in nome:
    nome = str(input('NOME INVÁLIDO! Digite novamente: '))
nasc = str(input('Qual a data do seu nascimento? '))
endr = str(input('Qual o seu endereço? '))
objt = str(input('Qual o seu objetivo? '))
painel('RESULTADO')
print(f'- Nome: {nome}\n- Data de nascimento: {nasc}\n- Endereço: {endr}\n- Objetivos: {objt}')
