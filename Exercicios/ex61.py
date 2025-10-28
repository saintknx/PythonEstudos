'''Exercício Python 61: Refaça o DESAFIO 51, 
lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.'''

# primeiro = int(input('Digite o primeiro termo: '))
# razao = int(input('Digite a razão: '))
# decimo = primeiro + (10 - 1) * razao
# for c in range(primeiro, decimo + razao, razao):
#     print(c)

primeiro = int(input('Digite o primeiro termo de uma PA: '))
razao = int(input('Digite a razão da PA: '))
decimo = primeiro + (10 - 1) * razao
c = primeiro
while c < decimo + razao:
    print('{} -> '.format(c), end='')
    c += razao
    if c == decimo + razao:
        print('FIM')


