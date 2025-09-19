valor = input('Digite um valor: ')
print('Valor numerico:', valor.isnumeric()) # retorna True se for numerico
print('Valor alfabetico:',valor.isalpha()) # retorna True se for alfabetico
print('Valor alfanumerico:',valor.isalnum()) # retorna True se for alfanumerico
print('Valor maiusculo:',valor.isupper()) # retorna True se for maiusculo
print('Valor minusculo:',valor.islower()) # retorna True se for minusculo
print('Valor capitalizado:',valor.istitle()) # retorna True se for capitalizado 
print('Valor decimal:', valor.isdecimal()) # retorna True se for decimal
print('Valor espaço:', valor.isspace()) # retorna True se for espaço
