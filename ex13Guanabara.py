salario = float(input('Digite o salário do funcionário: R$'))
# aumento = salario * 0.15 # somente calcula o aumento de 15%, e pode ser mais dificil para solicitar o valor do desconto ao usuário
novo = salario + (salario * 15 / 100)  # calcula o aumento de 15% e soma ao valor do salário
print('Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(salario, novo))	# mostra o novo salário com o aumento de 15%