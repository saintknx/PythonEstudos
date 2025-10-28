'''Exercício Python 63: 
Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:

0 – 1 – 1 – 2 – 3 – 5 – 8 '''

''' a ordem de números inteiros, que parte, normalmente, 
de zero e um no qual cada número seguinte corresponde a soma dos dois algarismos anteriores.'''


print('-=' * 15)
print('{:>25}'.format('SEQUENCIA DE FIBONACCI'))
print('-=' * 15)
num = int(input('Quantos termos você quer mostrar? '))
c = 0 # é possivel iniciar o contador em 3, ja que os dois primeiros termos ja são mostrados, mas optei por subtrair 2 do num
n1 = 0
n2 = 1
print('{} -> {} ->'.format(n1, n2), end=' ')
while c < num - 2: # subtrai 2 do num para compensar os dois primeiros termos
    n3 = n2 + n1 # N3 é a soma dos dois termos anteriores
    n1 = n2  # atualiza o valor de N1 para o proximo termo
    n2 = n3 # atualiza o valor de N2 para o proximo termo
    print('{} ->'.format(n3), end=' ') 
    c += 1 
print('Fim', end='')
