import math
catetoOposto = float(input('Digite o comprimento do cateto oposto:'))
catetoAdjacente = float(input('Digite o comprimento do cateto adjacente:'))
hipotenusa = math.hypot(catetoOposto, catetoAdjacente)
print('Cateto oposto:{}\nCateto adjacente:{}\nHipotenusa:{:.2f}'.format(catetoOposto, catetoAdjacente, hipotenusa))