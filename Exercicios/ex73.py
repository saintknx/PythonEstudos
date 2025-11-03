'''Crie uma tupla preenchida com os 20 primeiros colocados da tabela do campeonato brasileiro de futebol, na ordem de colocação, depois mostre:
A) Apenas os 5 primeiros colocados
B) Os ultimos 5 colocados da tabela.
C) Uma lista com os times em ordem alfabética.
D) Em que posição da tabela está o time da juventude'''

times = ('Palmeiras', 'Flamengo', 'Cruzeiro', 'Mirassol', 'Bahia', 'Botafogo', 'Fluminense', 'São Paulo', 'Vasco',
        'Corinthians', 'Grêmio', 'Ceará', 'Atlético', 'Bragantino', 'Internacional', 'Santos', 'EC Vitória', 'Fortaleza',
        'Juventude', 'Sport Recife')
print('-=' * 25)
print(f'Lista de times do brasileirão {times}')
print('-=' * 25)
print(f'Os 5 primeiros times são: {times[0:5]}')
print('-=' * 25)
print(f'Os 4 últimos são: {times[-4:]}')
print('-=' * 25)
print(f'Os times em ordem alfábetica são:{sorted(times)}')
print('-=' * 25)
print(f'O Juventude está {times.index('Juventude')}ª na posição ')