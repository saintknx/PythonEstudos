'''Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas
B) Uma listagem com as pessoas mais pesadas
c) Uma listagem com as pessoas mais leves'''
dados = list()
pessoas = list()
maior_peso = menor_peso = 0
while True:
    continuar = ' '
    pessoas.append(str(input('Nome: ')).title()) # Insere o nome na lista pessoas
    pessoas.append(float(input('Peso: ')))
    if len(dados) == 0: # Se for a primeira pessoa cadastrada, define o maior e menor peso como o peso dessa pessoa
        maior_peso = menor_peso = pessoas[1]
    else:
        if pessoas[1] > maior_peso:
            maior_peso = pessoas[1]
        if pessoas[1] < menor_peso:
            menor_peso = pessoas[1]
    dados.append(pessoas[:]) # Adiciona uma cópia da lista pessoas na lista dados
    pessoas.clear() # Limpa a lista pessoas para a próxima iteração
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).upper()[0]
    if continuar == 'N':
        break
print('-='*30)
print(f'Ao todo você cadastrou {len(dados)} pessoas.')
print(f'O maior peso foi de {maior_peso}KG. peso de ', end= '')
for p in dados:
    if p[1] == maior_peso:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {menor_peso}KG. peso de ', end= '')
for p in dados:
    if p[1] == menor_peso:
        print(f'[{p[0]}] ', end='')
print()

