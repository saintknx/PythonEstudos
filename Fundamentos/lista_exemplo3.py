a = [2,3,4,7]
b = a [:]# b referencia a mesma lista que A, ou seja, qualquer alteração em uma altera a outra B = A, mas com o slice b = a[:] cria uma cópia independente
b[2] = 8 
print(f'Lista A: {a}') 
print(f'Lista B: {b}')