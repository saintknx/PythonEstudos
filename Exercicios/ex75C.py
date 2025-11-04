tupla = (int(input('Digite um número: ')), 
        int(input('Digite outro número: ')), 
        int(input('Digite mais um número: ')), 
        int(input('Digite o ultimo número: ')))
print(f'Você digitou os valores: {tupla}')

print(f'O valor 9 apareceu {tupla.count(9)} vezes nessa tupla')

if 3 in tupla:
    print(f'O primeiro valor 3 apareceu na {tupla.index(3) + 1}ª posição')
else:
    print('Não foi digitado 3 em nenhuma posição')
    
print(f'Os valores pares da tupla são:', end=' ')
for valor in tupla:
    if valor % 2 == 0:
        print(valor, end=' ')