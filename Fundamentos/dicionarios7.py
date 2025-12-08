estado = {}
brasil = []
for c in range(0, 3):
    estado['uf'] = str(input(f'Unidade Federativa: '))
    estado['sigla'] = str(input(f'Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    # for k, v in e.items():
    #     print(f'O campo {k} tem valor {v}')
    for v in e.values():
        print(v, end=' ')
    print()
