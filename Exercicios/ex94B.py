pessoas = list()
pessoa = {}
soma = 0
while True:
    continuar = ' '
    pessoa['nome'] = str(input("Nome: ")).strip()
    pessoa['sexo'] = str(input("Sexo: ")).upper().strip()[0]
    if pessoa['sexo'] not in 'MmFf':
        while pessoa['sexo'] not in 'MmFf':
            print('Valor inválido! Digite apenas M ou F')
            pessoa['sexo'] = str(input("Sexo: ")).upper().strip()[0]
    pessoa['idade'] = int(input("Idade: "))
    soma += pessoa['idade']
    pessoas.append(pessoa.copy()) 
    # pessoa.clear() # Se usar o clear aqui, apaga os dados do dicionário que já foi adicionado na lista
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]: ')).upper()
        if continuar not in 'SN':
            print('Erro! Responda apenas com S ou N.')
    if continuar == 'N':
        break

print('-=' * 30)
media = soma/len(pessoas)
print(f'A) Ao todo temos {len(pessoas)} pessoas cadastradas.')
print(f'B) A média de idade é de {media} anos.')
print(f'C) As mulheres cadastradas foram: ')
for pessoa in pessoas:
    if pessoa['sexo'] == 'F':
        print(pessoa['nome'], end=' ')
print()
print(f'D) Lista das pessoas que estão acima da média: ')
for pessoa in pessoas:
    if pessoa['idade'] >= media:
        for k, v in pessoa.items():
            print(f'{k} = {v};', end=' ')
        print()
print('Fim.')