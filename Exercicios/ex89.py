'''Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.'''
classe = []
aluno = []
while True:
    continuar = ' ' 
    aluno.append(str(input('Nome: ')).title().strip())
    aluno.append(float(input('Nota 1: ')))
    aluno.append(float(input('Nota 2: ')))
    media = (aluno[1] + aluno[2]) / 2
    aluno.append(media)
    classe.append(aluno[:])   # Utilizei uma lista temporaria, e a composição de lista foi simples, preferi utilizar somente a regra de formatação [1:3] para mostrar as listas
    aluno.clear() 
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
    if continuar == 'N':
        break
print('-=' * 50)
print(f'{'No.':<10} {'NOME':^10} {'MEDIA':>10}')
print('-'* 40)
for aluno in classe:
    print(f'{classe.index(aluno):<10} {aluno[0]:^10} {aluno[3]:>10}')
print('-'*50)
while True:
    opcao = int(input('Mostrar as notas de qual aluno? (999 interrompe): '))
    if opcao == 999:
        break
    while opcao < 0 or opcao >= len(classe):
        opcao = int(input('Opcão fora do limite da classe, digite novamente a sua opção: '))
    print(f'As notas de {classe[opcao][0]} são {classe[opcao][1:3]}') 
    print('-' * 50)
print('Finalizando...')
print('<< VOLTE SEMPRE >>')
    