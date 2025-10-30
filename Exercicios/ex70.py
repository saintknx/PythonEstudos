'''Exercício Python 70: 
Crie um programa que leia o nome e o preço de vários produtos. 
O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato. '''
print('-'*20)
print(f'{'LOJA BARATA':^20}')
print('-'*20)
total = mil = contador = barato_preco = 0
barato_nome = ' '
while True:
    opcao = ' '
    nome = str(input('Nome do produto: ')).strip()
    preco = float(input('Preco do produto: R$'))
    total += preco
    if contador == 0:
        barato_nome = nome
        barato_preco = preco
    else:
        if preco < barato_preco:
            barato_preco = preco
            barato_nome = nome
    if preco > 1000:
        mil += 1
    contador += 1
    while opcao not in 'SN':
        opcao = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if opcao == 'N':
        break
print('--------Fim do programa----------')
print(f'O total gasto na compra foi de R${total:.2f}')
print(f'{mil} produtos custaram mais de R$1000')
print(f'O nome do produto mais barato é "{barato_nome.title()}" custando R${barato_preco:.2f}')