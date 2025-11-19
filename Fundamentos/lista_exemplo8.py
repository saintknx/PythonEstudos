galera = list()
dado = list()
totmaior = totmenor = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')).title()) #title() para deixar a primeira letra maiuscula
    dado.append(int(input('Idade:')))
    galera.append(dado[:]) # Se não houver [:], a lista 'dado' será referenciada e todas as alterações subsequentes afetarão todas as entradas em 'galera'
    dado.clear() # se nao houver o clear, a lista 'dado' continuará a crescer com os novos valores, resultando em entradas incorretas em 'galera'

for p in galera: #
    if p[1] >= 21:
        print(f'{p[0]} é maior de 21 anos.')
        totmaior += 1
    else:
        print(f'{p[0]} é menor de 21 anos.')
        totmenor += 1
        
print(f'Temos {totmaior} maiores e {totmenor} menores de 21 anos.')
