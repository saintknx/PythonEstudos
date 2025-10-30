from random import randint

print('=-' * 15)
print('VAMOS JOGAR PAR OU ÍMPAR') 
print('=-' * 15)

soma = cont = 0
venceu = False

while True:
    escolha = 'E'
    computador = randint(0, 10)
    
    valor = int(input('Digite um valor: '))
    
    while escolha not in 'PI':
        escolha = str(input('Par ou ímpar? [P/I]: ')).strip().upper()[0]  # Ortografia
    
    soma = valor + computador
    
    # Lógica simplificada
    if soma % 2 == 0:
        par_ou_impar = 'DEU PAR'
        venceu = (escolha == 'P')
    else:
        par_ou_impar = 'DEU ÍMPAR'  # Ortografia
        venceu = (escolha == 'I')
    
    print(f'Você jogou {valor} e o computador jogou {computador}. Total de {soma} {par_ou_impar}')
    
    if venceu:
        cont += 1
        print('Você venceu! \nVamos jogar novamente...')
        print('=-' * 15) 
    else:
        break

print('Você perdeu!')
print(f'Game Over, você venceu {cont} vezes')