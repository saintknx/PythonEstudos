'''Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e tambpem indique o menor e o maior valor que estão na tupla'''
from random import randint
tupla = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0, 10))
print('Os valores sorteados foram: ',end='')
for item in tupla:
    print(f'{item}',end=' ')
print(f'\nO menor valor da tupla é {min(tupla)}')
print(f'O maior valor da tupla é {max(tupla)}')