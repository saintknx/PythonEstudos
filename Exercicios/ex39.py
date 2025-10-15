'''Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe,
de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, 
se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''
from datetime import date
atual = date.today().year
dn = int(input('Informe seu ano de nascimento: '))
idade = atual - dn
print('Quem nasceu em {} tem {} anos em 2025'.format(dn, idade))
if idade < 18:
    if 18 - idade == 1:
        print('Ainda falta {} ano para o alistamento.'.format(18 - idade))
        print('Seu alistamento será em {}.'.format(atual + (18 - idade)))
    else:
        print('Ainda faltam {} anos para o alistamento'.format(18 - idade))
        print('Seu alistamento será em {}.'.format(atual + (18 - idade)))
elif idade > 18:
    if idade - 18 == 1:
        print('Você já deveria ter se alistado há {} ano.'.format(idade - 18))
        print('Seu alistamento foi em {}.'.format(atual - (idade - 18)))
    else:
        print('Você já deveria ter se alistado há {} anos.'.format(idade - 18))
        print('Seu alistamento foi em {}.'.format(atual - (idade - 18)))
else:
    print('Você tem que se alistar imediatamente.')