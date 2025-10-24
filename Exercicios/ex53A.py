frase = str(input('Digite uma frase: ')).upper().strip()
dividida = frase.split()
junto = ''.join(dividida)
invertido = ''
inverso = junto[::-1]
print('O inverso de {} é {}'.format(junto, invertido))
if junto == invertido: 
    print('A frase digitada é um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')