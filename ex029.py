#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h,
# mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.
velocidade = float(input('Qual é a sua velocidade em km/h ?'))
if velocidade <= 80 :
    print('Parabens viagem com segurança respeitando o limite da via 80km/h')
else :
    multa = (velocidade - 80) * 7.00
    print('Você foi multado e o valor da multa é R$ {:.2f} '.format(multa))



