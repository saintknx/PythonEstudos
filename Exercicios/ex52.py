'''Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo. '''
numero = int(input('Digite um número: '))
primo = False
contdiv = 0
for c in range (1, numero + 1):
    if numero % c == 0:
        contdiv += 1
        if contdiv > 2 or contdiv < 2:
            primo = False
        elif contdiv == 2:
            primo = True
print('O número {} é primo? {}'.format(numero, primo))