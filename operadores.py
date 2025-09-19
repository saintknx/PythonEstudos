n1 = int(input('Um valor: '))
n2 = int(input('Outro valor:'))
s = n1 + n2 # soma
m = n1 * n2 # multiplicação
d = n1 / n2 # divisão
di = n1 // n2 # divisão inteira
e = n1 ** n2 # potenciação
print('A soma é {}, o produto é {} e a divisão é {:.3f}'.format(s, m, d), end = ' ')
print('\nDivisão inteira {} a potência {}'.format(di, e))