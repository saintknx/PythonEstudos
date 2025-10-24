frase = str(input('Digite uma frase: ')).upper().strip()
dividida = frase.split()
junto = ''.join(dividida)
invertido = ''
for i in range(len(junto) - 1, -1, -1):   # Laço que adiciona a letra na posição do contador à variavel invertido.
    invertido += junto[i]
print('O inverso de {} é {}'.format(junto, invertido))
if junto == invertido: 
    print('A frase digitada é um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')