'''Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e tambpem indique o menor e o maior valor que estão na tupla'''
from random import randint
tupla = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0, 10))
print(f'A listagem de números da tupla é: {tupla}')
print(f'O menor valor da tupla é {min(tupla)}')
print(f'O maior valor da tupla é {max(tupla)}')