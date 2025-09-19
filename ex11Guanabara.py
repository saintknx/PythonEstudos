l = float(input('Digite a largura da parede:'))
h = float(input('Digite a altura da parede:'))
a = l * h
# tinta = a / 2
print('Sua parede tem a dimensão de {}x{} e sua área é de {:.3f}m²'.format(l, h, a))
print('Para pintar essa parede, você precisará de {}l de tinta'.format(a/2))