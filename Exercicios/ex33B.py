a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
c = int(input('Digite o terceiro valor: '))

menor = a
if b < menor:
    menor = b
if c < menor:
    menor = c

maior = a
if b > maior:
    maior = b
if c > maior:
    maior = c

print(f"Maior: {maior}")
print(f"Menor: {menor}")
