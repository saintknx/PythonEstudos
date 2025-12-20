'''Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. 
Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. 
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.'''
from datetime import date
ano_atual = date.today().year
dados = {}
dados['Nome'] = str(input('Nome: '))
ano_nasc = int(input('Ano de nascimento: '))
dados['Idade'] = ano_atual - ano_nasc
dados['CTPS'] = int(input('Carteira de trabalho (0 se não tiver): '))
if dados['CTPS'] != 0:
    dados['Contratação'] = int(input('Ano de contratação: '))
    anos_trabalhados = ano_atual - dados['Contratação']
    dados['Salário'] = float(input('Salário: '))
    dados['Aposentadoria'] = dados['Idade'] - anos_trabalhados + 35
print('-=' * 30)
for k, v in dados.items():
    print(f'- {k} tem o valor {v}')