lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
# Tuplas são imutáveis
lanche[1] = 'Refrigerante' # TypeError: 'tuple' object does not support item assignment
print(lanche)[1]