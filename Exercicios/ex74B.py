from random import randint
tupla = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0, 10))

# reinvenção da roda, pra casos especificos
maior = menor = tupla[0]
for numero in tupla:
    if numero > maior:
        maior = numero
    else:
        if numero < menor:
            menor = numero
print(tupla)
print(f"Maior: {maior}, Menor: {menor}")