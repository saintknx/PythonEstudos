'''Faça um programa que leia três números e mostre qual é o maior e qual é o menor.'''
a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
c = int(input('Digite o terceiro valor: '))
# Verifica qual é o menor valor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# Verifica qual é o maior valor
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print("Maior: {}".format(maior))
print("Menor: {}".format(menor))

# esse codigo tem um erro, no caso quando digitamos o primeiro valor como menor e os dois outros iguais e maiores, ele nao reconhece o maior
# ou quando digitamos o primeiro valor como maior e os dois outros iguais e menores, ele nao reconhece o menor
# o codigo em ex33B.py resolve esse problema