'''Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.'''
hvelho = ''
totidade = 0
totmulher21 = 0
hidade = 0
for c in range(1, 5):
    print('-=-=-{}ª PESSOA-=-=-'.format(c))
    nome = str(input('Nome: '.format(c))).strip()
    idade = int(input('Idade: '.format(c)))
    sexo = str(input('Sexo [M/F]: '.format(c))).strip().upper()
    totidade += idade
    if c == 1 and sexo[0] == 'M':
        hvelho = nome
        hidade = idade
    if sexo[0] == 'M' and idade > hidade:
        hvelho = nome 
        hidade = idade
    else:
        if sexo[0] == 'F' and idade < 20:
            totmulher21 += 1
print('A média de idade entre as 4 pessoas é de {}'.format(totidade / 4))
print('O homem mais velho é {} com {} anos'.format(hvelho.capitalize(), hidade))
print('Ao todo, a quantidade de mulheres com menos de 20 anos é {}'.format(totmulher21))