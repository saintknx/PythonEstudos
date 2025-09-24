num = int(input('Digite um número de 0 9999: '))
unidade = num // 1 % 10
dezena = num // 10 % 10
centena = num // 100 % 10
milhar = num // 1000 % 10
print ("Analisando o número {}".format(num))
print ("Sua Unidade é: {}".format(unidade))
print ("Sua Dezena é: {} ".format(dezena))
print ("Sua Centena é: {} ".format(centena))
print ("Seu milhar é: {}".format(milhar))
