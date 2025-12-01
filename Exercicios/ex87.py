lista_maior = []
lista_menor = []
soma_par = soma_coluna = 0
for c in range(0, 3):
    for i in range(0, 3):
        lista_menor.append(int(input(f'Digite o valor para [{c}, {i}]: ')))
    lista_maior.append(lista_menor[:])
    lista_menor.clear()
print('-=' * 30)
for c in range(0, 3):
    for i in range(0, 3):
        print(f'[{lista_maior[c][i]:^5}]', end='')
    print()
print('-=' * 30)
for c in range(0, 3):
    for i in range (0, 3):
        if lista_maior[c][i] % 2 == 0:
            soma_par += lista_maior[c][i]
        if i == 2:
            soma_coluna += lista_maior[c][i]
        if c == 1:
            maior = max(lista_maior[c])
print(f'A soma dos valores pares é: {soma_par}')
print(f'A soma dos valores da terceira coluna é: {soma_coluna}')
print(f'O maior valor da segunda linha é: {maior}')