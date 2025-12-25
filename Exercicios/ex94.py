'''Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, 
guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: 
A) Quantas pessoas foram cadastradas 
B) A média de idade 
C) Uma lista com as mulheres 
D) Uma lista de pessoas com idade acima da média'''
pessoas = list()
pessoa = {}
mulheres = list()
acima_media = list()
soma = 0
while True:
    continuar = ' '
    pessoa['nome'] = str(input("Nome: ")).strip()
    pessoa['sexo'] = str(input("Sexo: ")).upper().strip()[0]
    if pessoa['sexo'] not in 'MmFf':
        while pessoa['sexo'] not in 'MmFf':
            print('Valor inválido! Digite apenas M ou F')
            pessoa['sexo'] = str(input("Sexo: ")).upper().strip()[0]
    
    pessoa['idade'] = int(input("Idade: "))
    pessoas.append(pessoa.copy()) 
    # pessoa.clear() # Se usar o clear aqui, apaga os dados do dicionário que já foi adicionado na lista
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]: ')).upper()
        if continuar not in 'SN':
            print('Erro! Responda apenas com S ou N.')
    if continuar == 'N':
        break
print('-=' * 30)

for pessoa in pessoas:
    soma += pessoa['idade']
media = soma/len(pessoas)

for pessoa in pessoas:
    if pessoa['sexo'] == 'F':
        mulheres.append(pessoa['nome'])

for pessoa in pessoas:
    if pessoa['idade'] > media:
        acima_media.append(pessoa)
    
print(f'A) Ao todo temos {len(pessoas)} pessoas cadastradas.')
print(f'B) A média de idade é de {media} anos.')
print(f'C) As mulheres cadastradas foram: ')
for mulher in mulheres:
    print(mulher, end=' ')
print(f'D) Lista das pessoas que estão acima da média: ')

for pessoa in acima_media:
    for k, v in pessoa.items():
        print(f'  {k} = {v};', end=' ')
    print()
print('Fim.')