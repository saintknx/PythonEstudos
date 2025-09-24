from math import sin, cos, tan, radians
angulo = int(input('Digite um ângulo: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print('O ângulo {} tem o seno {:.2f}, cosseno {:.2f} e tangente {:.2f}'.format(angulo, seno, cosseno, tangente))	