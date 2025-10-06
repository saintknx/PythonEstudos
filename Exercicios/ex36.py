'''Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, 
o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.'''

print('=-' * 10)
print('Emprestimo bancário')
print('=-' * 10)
valor = float(input('Qual é o valor da casa? R$'))
salario = float(input('Qual é o salário do comprador? R$'))
anos = int(input('Em quantos anos pagará? '))
tp100 = salario * (30 / 100)
prestacao = valor / (anos * 12)
print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}'.format(valor, anos, prestacao))
if prestacao > tp100 :
    print('Empréstimo NEGADO') 
else:
    print('Empréstimo pode ser ACEITO')