num = soma = contador = 0
num = int(input('Digite um número [999 para PARAR]: ')) 
while num != 999:
    soma += num
    contador += 1
    num = int(input('Digite um número [999 para PARAR]: '))
print('Foram digitados {} números e a soma entre eles é {}'.format(contador, soma))