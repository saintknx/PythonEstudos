'''Crie um programa que tenha uma tupla totalmente preenchida por uma contagem por extenso, de zero até vinte.
Seu programa deverá ler um número digitado pelo teclado (entre 0 e 20) e mostrá-lo por extenso.'''
extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 
            'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 
            'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 
            'Dezesseis', 'Dezessete', 'Dezoito','Dezenove', 'Vinte')

numero = int(input('Para vê-lo escrito por extenso, digite um número de 0 até 20: '))
while numero > 20 or numero < 0:
    numero = int(input('Tente novamente, digite um número de 0 até 20: '))
print(f'Você digitou o número {numero}. Ele escrito por extenso é {extenso[numero]}')