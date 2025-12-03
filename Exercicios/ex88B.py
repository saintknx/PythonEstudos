'''Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.'''
from random import randint
from time import sleep
jogo_atual = []
todos_jogos = []
print('-' * 30)
print(f'{'JOGA NA MEGA SENA':^30}')
print('-' * 30)
quantidade = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'-=-=-= SORTEANDO {quantidade} JOGOS -=-=-=')
for jogos in range(1, quantidade + 1):
    for numeros in range (0, 6):
        aleatorio = randint(1,60)
        if numeros == 0: # Garante que o primeiro número seja adicionado sem verificação
            jogo_atual.append(aleatorio) # Adiciona o número gerado à lista do jogo atual
        else: # Para os próximos números, verifica se já existe na lista
            while aleatorio in jogo_atual: # Enquanto o número gerado já estiver na lista
                aleatorio = randint(1,60) # Gera um novo número
            jogo_atual.append(aleatorio) # Adiciona o número único à lista do jogo atual
    todos_jogos.append(jogo_atual[:]) 
    sleep(1)
    print(f'Jogo {jogos}: {sorted(todos_jogos[jogos - 1])}') 
    jogo_atual.clear()
print('-=-=-=-=-=-=-= BOA SORTE -=-=-=-=-=-=-=-=')