'''Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. 
Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.'''
numeros = []
while True:
    continuar = ' '
    numero = int(input('Digite um valor: '))
    if numero not in numeros:
        numeros.append(numero)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado, não vou adicionar...')
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if continuar == 'N':
        break
print('-=' * 30)
print(f'Você digitou os valores {sorted(numeros)}')
