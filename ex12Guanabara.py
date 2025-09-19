produto = float(input('Digite o preço do produto: R$'))
desconto = produto * 0.05 # somente calcula o desconto de 5%
# novo = produto - (preco * 5 / 100)  # calcula o desconto de 5% e subtrai do valor do produto
print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}'.format(produto, produto - desconto))	# pega o valor do produto e subtrai o desconto