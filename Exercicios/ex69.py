'''Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas. 
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos. '''
tot_18 = tot_homens = tot_mulher = 0
while True:
    sexo = opcao = '?'
    print('-' * 20)
    print('Cadastre uma pessoa')
    print('-' * 20)
    idade = int(input('Idade: '))
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    print('-' * 20)
    if idade >= 18:
        tot_18 += 1
    if sexo == 'M':
        tot_homens += 1
    if sexo == 'F' and idade < 20:
        tot_mulher += 1
    while opcao not in 'SN':
        opcao = str(input('Quer continuar? [S/N]: ')).strip().upper()
    if opcao == 'N':
        break
print(f'Ao todo, {tot_18} pessoas atingiram a maioridade ')
print(f'{tot_homens} homens foram cadastrados')
print(f'{tot_mulher} mulheres são menores de 20 anos ')