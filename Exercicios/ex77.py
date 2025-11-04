'''Exercício Python 077: 
Crie um programa que tenha uma tupla com várias palavras (não usar acentos). 
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.'''
palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR',
            'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')
for c in range(0, len(palavras)):
    print(f'Na palavra {palavras[c]} temos', end=' ')
    for letra in palavras[c]:
        if letra in 'AEIOU':
            print(letra, end=' ')
    print()
