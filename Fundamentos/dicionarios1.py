pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos') # Exemplo de exibição com formatação
print(pessoas.keys()) # Exibe as chaves // dict_keys(['nome', 'sexo', 'idade'])
print(pessoas.values()) # Exibe os valores // dict_values(['Gustavo', 'M', 22])
print(pessoas.items()) # Exibe todos os itens // dict_items([('nome', 'Gustavo'), ('sexo', 'M'), ('idade', 22)])