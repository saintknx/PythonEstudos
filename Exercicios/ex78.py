lista = []
for contador in range(0, 5):
    lista.append(int(input(f'Digite um valor para a Posição {contador}: ')))
print('=-' * 20)
maior = max(lista)
menor = min(lista)
print(f'Você digitou os valores {lista}')
print(f'O maior valor foi {maior} nas posições:',end=' ')
for i, v in enumerate(lista):
    if maior == v:
        print(i, end='...')
print(f'\nO menor valor digitado foi {menor} nas posições:', end= ' ')
for i, v in enumerate(lista):
    if menor == v:
        print(i, end= '...')

