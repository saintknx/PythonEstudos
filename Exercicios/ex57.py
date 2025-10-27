'''Exercício Python 57: Faça um programa que leia o sexo de uma pessoa, 
mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.'''
sexo = str(input('Digite o seu sexo [M/F]: ')).upper().strip() [0] # [0] pega a primeira letra
while sexo not in ['M', 'F']:
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).upper().strip() [0]
print('Sexo {} registrado com sucesso.'.format(sexo))