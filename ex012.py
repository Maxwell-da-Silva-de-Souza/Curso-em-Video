#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
preço = float(input('Digite o valor do produto !! R$'))
desconto = preço - (preço * 5 / 100)
print (' O preço do produto é R$ {:.2f} com desconto de 5% R${:.2f} '.format(preço, desconto))