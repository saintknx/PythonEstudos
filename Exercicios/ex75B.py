a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))
c = int(input('Digite mais um número: '))
d = int(input('Digite o ultimo número: '))

tupla = (a, b, c, d)
tem_par = any(num % 2 == 0 for num in tupla)

print(f'Você digitou os valores: {tupla}')
print(f'O valor 9 apareceu {tupla.count(9)} vezes nessa tupla')

if 3 in tupla:
    print(f'O primeiro valor 3 apareceu na {tupla.index(3) + 1}ª posição')
else:
    print('Não foi digitado 3 em nenhuma posição')

if not tem_par:
    print('Não há valores pares na tupla')
else:
    print('Os valores pares na tupla são: ', end='')
    for numero in tupla:
        if numero % 2 == 0:
            print(numero, end=' ')
