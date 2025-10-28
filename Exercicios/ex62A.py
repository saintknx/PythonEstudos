print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
resposta = 10
tot_termos = 0
termo = primeiro
while resposta != 0:
    contador = 1
    while contador <= resposta:
        print('{} -> '.format(termo), end='')
        termo += razao
        contador += 1
        tot_termos += 1
    print('PAUSA')
    resposta = int(input('Quantos valores a mais quer mostrar? '))
print('Progressão finalizada com {} termos mostrados'.format(tot_termos))