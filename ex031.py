# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km
# e R$0,45 parta viagens mais longas.
from time import sleep
distancia = float(input('Qual é a distancia da sua viagem em km ?'))
sleep(1)
if distancia <= 200 :
    preço = distancia * 0.50
else:
    preço = distancia * 0.45
print('O valor da sua viagem é de R$ {:.2f}'.format(preço))


