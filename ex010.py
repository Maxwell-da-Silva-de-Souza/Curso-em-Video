#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
# e mostre quantos dólares ela pode comprar.
n = float(input('Digite o valor que você tem!!'))#real
d = n/5.57#dolar
e = n/6.21#euro
print('Você tem {:.2f} reais e pode trocar por {:.2f} dolares e {:.2f} euros'.format(n, d, e))