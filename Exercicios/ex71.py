print('=' * 30)
print(f'{'Banco CEV':^30}')
print('=' * 30)
valor = int(input('Digite o valor a ser sacado: R$'))
total = valor
ced = 50
total_ced = 0
while True:
    if total >= ced:
        total -= ced
        total_ced += 1
    else:  
        print(f'Total de {total_ced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        total_ced = 0
        if total == 0:
            break
print('=' * 30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')