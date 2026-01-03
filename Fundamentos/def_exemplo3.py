def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')


# Programa principal
soma (4, 5) # Caso não for indicado ele usa os parametros na ordem: primeiro valor = A, segundo valor = B
soma (b=4, a=5) # B = indicado como 4, A = indicado como 5
# soma (b=4, 5) Erro de sintaxe