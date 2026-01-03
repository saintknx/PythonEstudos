def area(l, c):
    a = l * c
    print(f'A área de um terreno {l}x{c} é de {a}m².')
    
    
#Programa principal
print()
print('Controle de Terrenos')
print('-'*30)
largura = float(input('Largura(m):'))
comprimento = float(input('Comprimento(m):'))
area(largura, comprimento)
