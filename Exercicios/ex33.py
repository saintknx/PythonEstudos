'''Faça um programa que leia três números e mostre qual é o maior e qual é o menor.'''
a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
c = int(input('Digite o terceiro valor: '))
maior = a
menor = a
# Verifica qual é o maior valor
if b > maior and b > c:
    maior = b
if c > maior and c > b:
    maior = c
# Verifica qual é o menor valor
if b < menor and b < c:
    menor = b
if c < menor and c < b:
    menor = c

print("Maior: {}".format(maior))
print("Menor: {}".format(menor))

# esse codigo tem um erro, no caso quando digitamos o primeiro valor como menor e os dois outros iguais e maiores, ele nao reconhece o maior
# ou quando digitamos o primeiro valor como maior e os dois outros iguais e menores, ele nao reconhece o menor
# o codigo em ex33B.py resolve esse problema

