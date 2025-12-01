'''Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3×3 e 
preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.'''
lista_maior = []
lista_menor = []
for c in range(0, 3):
    for i in range(0, 3):
        lista_menor.append(int(input(f'Digite o valor para [{c}, {i}]: ')))
    lista_maior.append(lista_menor[:])
    lista_menor.clear()
print('-=' * 30)
for lista in lista_maior:
    print(f'[{lista[0]:^5}] [{lista[1]:^5}] [{lista[2]:^5}]')