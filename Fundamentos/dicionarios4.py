pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
pessoas['nome'] = 'Leandro' # Renomeando
for k, v in pessoas.items():
    print(f'{k} = {v}')