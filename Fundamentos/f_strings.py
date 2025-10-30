n = soma = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    soma += n
# print('A soma vale {}'.format(soma))
print(f'A soma vale {soma}') # interpolação dentro de strings
