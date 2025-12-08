pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
pessoas['peso'] = 98.5 # adicionando nova key e valor
for k, v in pessoas.items():
    print(f'{k} = {v}')