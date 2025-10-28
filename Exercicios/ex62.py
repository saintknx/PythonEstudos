"""Exercício Python 62: Melhore o DESAFIO 61, 
perguntando para o usuário se ele quer mostrar mais alguns termos. 
O programa encerrará quando ele disser que quer mostrar 0 termos. """

print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
resposta = 10
while resposta != 0:
    cont = 1
    while cont <= resposta:
        print('{} -> '.format(termo), end='')
        termo += razao
        cont += 1
    resposta = int(input('Quantos termos a mais você quer mostrar? '))
print('FIM')
