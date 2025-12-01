lista_maior = []
lista_menor = []
soma_par = soma_coluna = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        lista_menor.append(int(input(f'Digite o valor para [{linha}, {coluna}]: ')))
    lista_maior.append(lista_menor[:])
    lista_menor.clear()
print('-=' * 30)
for linha in range(0, 3): # Loop para exibir
    for coluna in range(0, 3):
        print(f'[{lista_maior[linha][coluna]:^5}]', end='')
    print()
print('-=' * 30)
for linha in range(0, 3): # Loop para cálculos
    for coluna in range (0, 3):
        if lista_maior[linha][coluna] % 2 == 0:
            soma_par += lista_maior[linha][coluna]
        if coluna == 2:
            soma_coluna += lista_maior[linha][coluna]
        if linha == 1:
            maior = max(lista_maior[linha])

print(f'A soma dos valores pares é: {soma_par}')
print(f'A soma dos valores da terceira coluna é: {soma_coluna}')
print(f'O maior valor da segunda linha é: {maior}')