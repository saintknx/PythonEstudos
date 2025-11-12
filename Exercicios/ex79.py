'''Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. 
Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.'''
numeros = []
cont = 0
while True:
    continuar = ' '
    numero = int(input('Digite um valor: '))
    if cont == 0:
        numeros.append(numero)
        print('Valor adicionado com sucesso...')
        cont += 1
    else:
        for valor in numeros:
            if numero in numeros:
                print('Valor duplicado, não vou adicionar...')
                break
            else:
                numeros.append(numero)
                print('Valor adicionado com sucesso...')
                break
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if continuar == 'N':
        break
print('-=' * 30)
print(f'Você digitou os valores {sorted(numeros)}')
    