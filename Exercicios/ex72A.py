'''Crie um programa que tenha uma tupla totalmente preenchida por uma contagem por extenso, de zero até vinte.
Seu programa deverá ler um número digitado pelo teclado (entre 0 e 20) e mostrá-lo por extenso.'''
extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 
            'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 
            'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 
            'Dezesseis', 'Dezessete', 'Dezoito','Dezenove', 'Vinte')
while True:
    opcao = ' '
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        print(f'Você digitou o número {extenso[num]}')
        while opcao not in 'SN':
            opcao = str(input('Você quer continuar? [S/N]: ')).upper().strip()[0]
        if opcao == 'N':
            break
    else:   
        print('Tente novamente. ', end='')
print('FIM DO PROGRAMA')
