'''Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores, 
incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.'''
gols = list()
jogador = dict()
jogadores = list()
while True:
    continuar = ' '
    jogador['Nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Partidas jogadas pelo {jogador["Nome"]}: '))
    for c in range(0, partidas):
        gols.append(int(input(f'Gols na partida {c+1}: ')))
    jogador['Gols'] = (gols[:])
    jogador['Total'] = sum(gols)
    jogadores.append(jogador.copy())
    gols.clear()
    jogador.clear()
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]: ')).upper().strip()[0] # flag
    if continuar == 'N':
        break
print('-=' * 30)
print(f'{"Cod":<5} {"Nome":<20} {"Gols":<20} {"Total":>5}')
print('--' * 30)
for i, jogador in enumerate(jogadores):
    gols = str(jogador['Gols'])
    print(f'{i:<5} {jogador["Nome"]:<20} {gols:<25} {jogador["Total"]:<5}')
print('-=' * 30)
while True:
    resposta = -1
    while resposta >= len(jogadores) or resposta < 0:
        resposta = int(input('Mostrar dados de qual jogador? (999 para parar) '))
        if resposta == 999: 
            break      
        if resposta >= len(jogadores) or resposta < 0:
            print(f'Resposta inválida. Não há jogador com código {resposta}')
            print('-='*30)
    if resposta == 999: 
        break
    print(f'-- LEVANTAMENTO DO JOGADOR {jogadores[resposta]["Nome"]}:')
    for i, jogo in enumerate(jogadores[resposta]['Gols']):
        print(f'No jogo {i + 1} fez {jogo} gols.')
    print('--'*30)
print('<< VOLTE SEMPRE >>')
