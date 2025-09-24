frase = 'Curso em Vídeo Python'
print(frase.split()) # separa as palavras em uma lista
dividido = frase.split()
print(dividido[0]) # Curso
print(dividido[2][3]) # Retorna 'e' da palavra 'Vídeo'
print('-'.join(dividido))
