num = [2, 5 , 9, 1]
num[2] = 3 # Alterando o valor do índice 2
num.append(7) # Adicionando o valor 7 no final da lista
# num.sort() # Colocando a lista em ordem crescente
num.sort(reverse=True) # Colocando a lista em ordem decrescente
num.insert(2, 2) # Adicionando o valor 2 no índice 2
num.remove(2) # Removendo o valor 2 da lista (apenas o primeiro encontrado)
if 4 in num:
    num.remove(4) # Removendo o valor 4 da lista se ele existir
else:
    print('Não achei o número 4 na lista.')
# num.pop() # Removendo o último valor da lista
# num.pop(2) # Removendo o valor do índice 2
print(num)
print(f'Essa lista tem {len(num)} elementos.') # Mostrando a quantidade de elementos na lista
