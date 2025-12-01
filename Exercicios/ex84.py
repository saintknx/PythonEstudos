'''Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas
B) Uma listagem com as pessoas mais pesadas
c) Uma listagem com as pessoas mais leves'''
dados = list()
pessoas = list()
tot_pessoas = 0
pesados = []
leves = []
while True:
    continuar = ' '
    pessoas.append(str(input('Nome: ')).title()) # Insere o nome na lista pessoas
    pessoas.append(float(input('Peso: ')))
    dados.append(pessoas[:]) # Adiciona uma cópia da lista pessoas na lista dados
    tot_pessoas += 1
    if len(dados) == 1: # Se for a primeira pessoa cadastrada, define o maior e menor peso como o peso dessa pessoa
        maior_peso = menor_peso = dados[0] # Armazena a primeira pessoa como maior e menor peso
    pessoas.clear() # Limpa a lista pessoas para a próxima iteração
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).upper()[0]
    if continuar == 'N':
        break
for p in dados:  # Percorre a lista de dados para encontrar o maior e menor peso
    if p[1] > maior_peso[1]:
        maior_peso = p
    if p[1] < menor_peso[1]:
        menor_peso = p
for p in dados: # Percorre a lista de dados para encontrar todas as pessoas com o maior e menor peso
    if maior_peso[1] == p[1]:
        pesados.append(p[0])
    if menor_peso[1] == p[1]:
        leves.append(p[0])

print('-='*30)
print(f'Ao todo você cadastrou {tot_pessoas} pessoas.')
print(f'O maior peso foi de {maior_peso[1]}KG. peso de {pesados}')
print(f'O menor peso foi de {menor_peso[1]}KG. peso de {leves}')

