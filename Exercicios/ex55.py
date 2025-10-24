'''Exercício Python 55: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.'''
maior = 0
menor = 0
for i in range(1, 6):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(i)))
    if i == 1:
        maior = peso
        menor = peso
    elif peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso

print('Menor: {}'.format(menor))
print('Maior: {}'.format(maior))