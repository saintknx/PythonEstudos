resposta = 'S'
laco = soma = media = menor = maior = 0
while resposta in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    laco += 1
    if laco == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resposta = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
media = soma/laco
print('O maior valor lido foi {} e o menor foi {}'.format(maior, menor))
print('A média entre os {} valores digitados foi {}'.format(laco, media))