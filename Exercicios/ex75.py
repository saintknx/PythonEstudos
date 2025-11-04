'''Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os numeros pares.'''
a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))
c = int(input('Digite mais um número: '))
d = int(input('Digite o ultimo número: '))
tupla = (a, b, c, d)
print(f'Você digitou os valores: {tupla}')

print(f'O valor 9 apareceu {tupla.count(9)} vezes nessa tupla')

if 3 in tupla:
    print(f'O primeiro valor 3 apareceu na {tupla.index(3) + 1}ª posição')
else:
    print('Não foi digitado 3 em nenhuma posição')
    
print(f'Os valores pares da tupla são:', end=' ')
for c in range(0, len(tupla)):
    if tupla[c] % 2 == 0:
        print(tupla[c], end=' ')
