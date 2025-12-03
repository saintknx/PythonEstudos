'''Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.'''
from random import randint
jogo_atual = []
todos_jogos = []
print('-' * 30)
print(f'{'JOGA NA MEGA SENA':^30}')
print('-' * 30)
quantidade = int(input('Quantos jogos você quer que eu sorteie? '))
print('-=-=-= SORTEANDO 5 JOGOS -=-=-=')
for jogos in range(1, quantidade + 1):
    for numeros in range (0, 6):
        aleatorio = randint(1,60)
        if numeros == 0: 
            jogo_atual.append(aleatorio)
        else: 
            while aleatorio in jogo_atual:
                aleatorio = randint(1,60) 
            jogo_atual.append(aleatorio)
    todos_jogos.append(jogo_atual[:]) 
    print(f'Jogo {jogos}: {sorted(todos_jogos[jogos - 1])}')
    jogo_atual.clear()
print('-=-=-=-=-=-=-= BOA SORTE -=-=-=-=-=-=-=-=')