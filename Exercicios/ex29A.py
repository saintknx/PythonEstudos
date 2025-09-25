velocidade = float(input('Digite a velocidade do carro: '))
if velocidade > 80:  # Se estiver acima do limite
    multa = (velocidade - 80) * 7.0 # Calcula o valor da multa
    print('Multado! Você excedeu o limite permitido de 80KM/h \nVocê deverá pagar uma multa de R${:.2f}!'.format(multa)) # Informa o valor da multa
print('Tenha um bom dia, dirija com segurança')