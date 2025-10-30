from random import randint
print('=-' * 15)
print('VAMOS JOGAR PAR OU IMPAR ')
print('=-' * 15)
soma = cont = 0
venceu = bool()
par_ou_impar = ''
while True:
    escolha = 'E'
    valor = int(input('Digite um valor: '))
    computador = randint(0, 10)
    soma = valor + computador
    while escolha not in 'PI':
        escolha = str(input('Par ou impar? [P/I]: ')).strip().upper()[0]
        print(f'Você jogou {valor} e o computador jogou {computador}. Total de {soma} {par_ou_impar}')
    if soma % 2 == 0: # Par
        par_ou_impar = 'DEU PAR'
        if escolha == 'P': # Se o jogador escolheu par
            venceu = True # Jogador vence
            cont += 1
        else: 
            venceu = False # Jogador perde
            break
    else: # Impar
        par_ou_impar = 'DEU IMPAR'
        if escolha == 'I': # Se o jogador escolheu impar
            venceu = True  # Jogador vence
            cont += 1
        else:
            venceu = False # Jogador perde
            break
    print('Você venceu! \nVamos jogar novamente...')
print('Você perdeu!')
print(f'Game Over, você venceu {cont} vezes')