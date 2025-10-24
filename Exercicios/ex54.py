'''Exercício Python 54: 
Crie um programa que leia o ano de nascimento de sete pessoas. 
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.'''
from datetime import date
maior = 0
menor = 0
atual = date.today().year
for i in range(1, 8):
    datapessoa = int(input('Ano que a {}ª pessoa nasceu: '.format(i)))
    if atual - datapessoa >= 18:
        maior += 1
    else:
        menor += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(maior))
print('E também tivemos {} pessoas menores de idade'.format(menor))
