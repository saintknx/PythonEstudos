galera = list()
dado = list()
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade:')))
    galera.append(dado[:]) # Se não houver [:], a lista 'dado' será referenciada e todas as alterações subsequentes afetarão todas as entradas em 'galera'
    dado.clear() # se nao houver o clear, a lista 'dado' continuará a crescer com os novos valores, resultando em entradas incorretas em 'galera'
print(galera)
