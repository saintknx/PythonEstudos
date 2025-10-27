from random import randint
computador = randint(0, 10)
acertou = False
print('''Sou seu computador...
Acabei de pensar em número entre 0 e 10.
Consegue adivinhar?''')
tentativas = 0
while acertou == False: # while not acertou:
    jogador = int(input('Qual é seu palpite: '))
    tentativas += 1
    if jogador < computador:
        print('Mais... Tente novamente')
    elif jogador > computador:
        print('Menos... Tente novamente')
    else: 
        acertou = True
print('Parabéns, você acertou o número! Foram necessárias {} tentativas'.format(tentativas))
