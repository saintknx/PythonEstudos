teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:]) #copia dos dados de teste, se eu não colocar o [:], ele referencia o mesmo local na memória
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:]) #copia dos dados de teste
print(galera)