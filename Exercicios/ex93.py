'''Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. 
Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.'''
gols = list()
# soma = 0
jogador = dict()
jogador['Nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Partidas jogadas pelo {jogador["Nome"]}: '))
for c in range(0, partidas):
    gols.append(int(input(f'Gols na partida {c+1}: ')))
jogador['Gols'] = (gols)

# for g in gols:
#     soma += g

# jogador['Total'] = soma
jogador['Total'] = sum(gols)
print('-=' * 30)
print(jogador)
print('-=' * 30)

for k, v in jogador.items():
    print(f'O campo {k}, tem o valor {v}')
print('-=' * 30)

print(f'O jogador {jogador["Nome"]} jogou {partidas} partidas')
for i, g in enumerate(gols):
    print(f'  => Na partida {i + 1}, fez {g} gols.')
print(f'Foi um total de {jogador['Total']} gols.')