def escreva(texto):
    tamanho = len(texto) + 4
    print('~' * tamanho)
    print(texto.center(tamanho))
    print('~' * tamanho)


escreva('Gustavo Guanabara')
escreva('Curso de Python no Youtube')
escreva('CeV')
