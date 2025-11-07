valores = [] # Cria uma lista vazia para armazenar os valores, pode ser criada assim ou com valores = list()
valores.append(5)
valores.append(9)
valores.append(4)
# for valor in valores:  # Itera sobre cada valor na lista 'valores'
#     print(f'{valor}...', end='')  # Imprime cada valor seguido de '...'
for c, v in enumerate(valores):  # Itera sobre a lista 'valores' com índice e valor
    print(f'Na posição {c} encontrei o valor {v}!')  # Imprime a posição e o valor correspondente
print('Cheguei ao final da lista.')  # Indica que a iteração sobre a lista foi concluída'