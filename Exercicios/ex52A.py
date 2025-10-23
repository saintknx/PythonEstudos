'''Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo. '''
numero = int(input('Digite um número: '))
contdiv = 0
for c in range (1, numero + 1):
    print(c, end=' ')
    if numero % c == 0:
        contdiv += 1
print('\nO número {} é divisivel por {} valores'.format(numero, contdiv,))
if contdiv == 2:
    print('Por isso ele É PRIMO')
else:
    print('Por isso ele NÃO É PRIMO')