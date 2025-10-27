'''Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. 
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.'''

from random import randint
computador = randint(0, 10)
print('''Sou seu computador...
Acabei de pensar em número entre 0 e 10.
Consegue adivinhar?''')
jogador = int(input('Digite um número entre 0 e 10: '))
tentativas = 1
while jogador != computador:
    if jogador < computador:
        print('Mais... Tente novamente')
    else:
        print('Menos... Tente novamente')
    jogador = int(input('Qual é seu palpite: '))
    tentativas += 1
print('Parabéns, você acertou o número! Foram necessárias {} tentativas'.format(tentativas))

