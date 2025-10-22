'Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.'
import random
from time import sleep
opcoes = ['Pedra', 'Papel', 'Tesoura']
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Digite sua jogada: '))
if jogador in (0, 1, 2):
    computador = random.randint(0,2)
    sleep(1)
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO')
    print('=-' * 15)
    print('Jogada do jogador: {}'.format(opcoes[jogador]))
    print('Jogada do computador: {}'.format(opcoes[computador]))
    print('=-' * 15)
    if jogador == 0: # Jogador pedra
        if computador == 0: # Computador pedra
            print('EMPATE')
        elif computador == 1: # Computador papel
            print('COMPUTADOR VENCE')
        elif computador == 2: # Computador tesoura
            print('JOGADOR VENCE')
    elif jogador == 1: # Jogador Papel
        if computador == 0: # Computador pedra
            print('JOGADOR VENCE')
        elif computador == 1: # Computador Papel
            print('EMPATE')
        elif computador == 2: # Computador tesoura
            print('COMPUTADOR VENCE')
    elif jogador == 2: # Jogador Tesoura
        if computador == 0: # Computador pedra
            print('COMPUTADOR VENCE')
        elif computador == 1: # Computador Papel
            print('JOGADOR VENCE')
        elif computador == 2: # Computador tesoura
            print('EMPATE')
else: 
    print('Jogada inválida, tente novamente.')