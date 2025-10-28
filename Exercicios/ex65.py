'''Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado. 
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''
resposta = 'S'
laco = soma = 0
while resposta != 'N':
    laco += 1
    num = int(input('Digite um número: '))
    soma += num
    if laco == 1:
        maior = menor = num
        # maior = num 
        # menor = num
    elif laco != 1 and num > maior:
        maior = num
    elif laco != 1 and num < menor:
        menor = num
    resposta = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
print('O maior valor lido foi {} e o menor foi {}'.format(maior, menor))
print('A média entre os {} valores digitados foi {}'.format(laco, soma/laco))
