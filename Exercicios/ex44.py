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
if opcao == 1:
    print('Opção escolhida: À vista dinheiro/cheque')
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, preco - preco * 10 / 100))
elif opcao == 2:
    print('Opção escolhida: À vista cartão')
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, preco - preco * 5 / 100))
elif opcao == 3:
    print('Opção escolhida: 2x no cartão')
    print('Sua compra de R${:.2f} será parcelada em 2x de R${:.2f}'.format(preco, preco / 2))
elif opcao == 4:
    print('Opção escolhida: 3x ou mais no cartão')
    parcelas = int(input('Número de parcelas: '))
    print('Sua compra será parcelada em {} vezes de R${:.2f} COM JUROS'.format(parcelas, (preco + preco * 20 / 100) / parcelas))
    print('Sua compra de R${:.2f} vai custar {:.2f} no final.'.format(preco, preco + preco * 20 / 100))