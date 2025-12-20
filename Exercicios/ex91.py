'''Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. 
No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.'''

from random import randint
from time import sleep
resultados = {'jogador1': randint(1,6), 'jogador2': randint(1,6), 'jogador3': randint(1,6), 'jogador4': randint(1,6) } 
print('Valores sorteados: ')
for k, v in resultados.items():
    print(f'    {k} tirou {v}.')
    sleep(1)
print('Ranking dos jogadores: ')
ordenado = dict(sorted(resultados.items(),key=lambda item: item[1], reverse=True))
for posicao, (jogador, valor) in enumerate(ordenado.items(), start=1): # Da uma oiada depois, interessante
    print(f'{posicao}º lugar: {jogador} com {valor}')
    sleep(1)
