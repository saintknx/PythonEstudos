from random import randint
from time import sleep
resultados = {'jogador1': randint(1,6), 'jogador2': randint(1,6), 'jogador3': randint(1,6), 'jogador4': randint(1,6) }
print('Valores sorteados: ')
for k, v in resultados.items():
    print(f'    {k} tirou {v}.')
    sleep(1)
print('Ranking dos jogadores: ')
ranking = dict(sorted(resultados.items(), key=lambda item: item[1], reverse=True))
cont = 1
for k, v in ranking.items():
    print(f'    {cont}º Lugar:',end=' ')
    print(f'{k} com {v}')
    cont += 1
    sleep(1)