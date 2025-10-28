'''Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:

5! = 5 x 4 x 3 x 2 x 1 = 120'''
num = int(input('Digite um número para calcular seu Fatorial: '))
c = num
fatorial = 1
while c != 0:
    # fatorial += fatorial * (c - 1)
    # fatorial = fatorial + fatorial * (c - 1)
    fatorial *= c
    if c == num:
        print(c,'x', end=' ')
    elif c != 1:
        print(c,'x', end=' ')
    elif c == 1:
        print(c,'=', end=' ')
    c -= 1
print(fatorial)

