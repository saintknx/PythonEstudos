num = int(input('Digite um valor: '))
contdiv = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end='')
        contdiv += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\n\033[mO número {} foi divisível por {} números.'.format(num, contdiv))
if contdiv == 2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')