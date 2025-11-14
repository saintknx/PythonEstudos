'''Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, 
crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. 
Ao final, mostre o conteúdo das três listas geradas.'''
lista = []
lista_par = []
lista_impar = []
while True:
    continuar = ' '
    lista.append(int(input('Digite um valor: ')))
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
for valor in lista:
    if valor % 2 == 0:
        lista_par.append(valor)
    elif valor % 2 != 0:
        lista_impar.append(valor)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {lista_par}')
print(f'A lista de impares é {lista_impar}')

