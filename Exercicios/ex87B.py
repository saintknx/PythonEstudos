soma_par = soma_coluna = 0
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite o valor para [{linha}, {coluna}]: '))
print('-=' * 30)
for linha in range(0, 3): # Loop para exibir
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()
for linha in range(0, 3): # Loop para cálculos
    for coluna in range (0, 3):
        if matriz[linha][coluna] % 2 == 0:
            soma_par += matriz[linha][coluna]
        if coluna == 2:
            soma_coluna += matriz[linha][coluna]
        if linha == 1:
            maior = max(matriz[linha])

print(f'A soma dos valores pares é: {soma_par}')
print(f'A soma dos valores da terceira coluna é: {soma_coluna}')
print(f'O maior valor da segunda linha é: {maior}')
