nome = str(input('Qual é o seu nome? ')).strip().title()
if nome == 'Kauã': 
    print('Que nome lindo você tem!')
elif nome == 'Maria' or nome == 'Luiza' or nome == 'Joana':
    print('Seu nome é muito popular no Brasil!')
elif nome in 'Ana Claudia Jessica Juliana':
    print('Belo nome feminino!')
else:
    print('Seu nome é tão normal!')
print('Bom dia, {}!'.format(nome))