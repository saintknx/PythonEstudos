'''Exercício Python 48: Faça um programa que calcule a soma entre todos os números impares que são múltiplos de três e que se encontram no intervalo de 1 até 500.'''
soma = 0
contador = 0
for c in range(3, 501, 6):
    if c % 3 == 0:
        contador += 1
        soma = soma + c
print('A soma dos {} valores solicitados é {}'.format(contador, soma))