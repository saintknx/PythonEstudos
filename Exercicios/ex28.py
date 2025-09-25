from random import randint
from time import sleep
aleatorio = randint(0, 5) # Gera um número aleatório entre 0 e 5
print ('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print ('-=-' * 20)
numero = int(input('Em que número pensei? ')) # Pede para o usuário tentar adivinhar o número
print('PROCESSANDO...')
sleep(2) # Pausa o programa por 2 segundos para criar um efeito de suspense
if numero == aleatorio: # Verifica se o número digitado é igual ao número aleatório
    print('Parabéns! Você acertou o número em que pensei, era {}'.format(aleatorio))
else:
    print('Você errou, tente de novo :( \nEu pensei no número {}'.format(aleatorio))