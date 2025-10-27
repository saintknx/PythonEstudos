'''Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso. '''

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
print('''[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos números
[ 5 ] Sair do programa''')
opcao = int(input('>>> Digite sua opção: '))
while opcao != 5: 
    if opcao == 1:
        print('A soma entre {} + {} = {}'.format(n1, n2, n1 + n2))
    elif opcao == 2:
        print('A multiplicação entre {} x {} = {}'.format(n1, n2, n1 * n2))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('O maior número entre {} e {} é {}'.format(n1, n2, maior))
    elif opcao == 4:
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
    else:
        print('Opção inválida, tente novamente.')
    print('-=' * 20)
    print('''[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos números
[ 5 ] Sair do programa''')
    opcao = int(input('>>> Digite sua opção: '))
print('Finalizando o programa... Até logo!')