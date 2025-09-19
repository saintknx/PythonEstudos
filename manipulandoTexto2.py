frase = 'Curso em Vídeo Python'
print(len(frase)) # tamanho da frase
print(frase.count('o')) # numero de 'o'
print(frase.count('o', 0, 13)) # numero de 'o' de 0 a 13
print(frase.find('deo')) # onde no indice começa 'deo'
print(frase.find('Android')) # não existe 'Android então retorna -1'
print('Curso' in frase) # retorna true se existe 'Curso' na frase
