'''Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

– à vista dinheiro/cheque: 10% de desconto

– à vista no cartão: 5% de desconto

– em até 2x no cartão: preço formal 

– 3x ou mais no cartão: 20% de juros'''
print('=' * 10)
print('{:>7}'.format('LOJA'))
print('=' * 10)
preco = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
=============================
[ 1 ] à vista dinheiro/cheque 
[ 2 ] à vista cartão
[ 3 ] 2x no cartão 
[ 4 ] 3x ou mais no cartão
=============================''') 
opcao = int(input('Qual é a opção? '))
if opcao in [1,2,3,4]:
    if opcao == 1:
        print('Opção escolhida: À vista dinheiro/cheque')
        total = preco - (preco * 10 / 100)
    elif opcao == 2:
        print('Opção escolhida: À vista cartão')
        total = preco - (preco * 5 / 100)
    elif opcao == 3:
        print('Opção escolhida: 2x no cartão')
        total = preco 
        parcela = total / 2
        print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS'.format(parcela))
    elif opcao == 4:
        print('Opção escolhida: 3x ou mais no cartão')
        parcela = int(input('Número de parcelas: '))
        total = preco + (preco * 20 / 100)
        print('Sua compra será parcelada em {} vezes de R${:.2f} COM JUROS'.format(parcela, total / parcela))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, total))
else:
    print('Opção inválida, tente novamente')