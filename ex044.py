#44: Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
print('{:=^40}'.format(' MAXX LOJA '))
preço = float(input('Qual é o valor da compra ? (R$)'))
print('Condições  de pagamento.')
print('''Condição 1: à vista dinheiro/cheque: 10% de desconto
Condição 2: à vista no cartão: 5% de desconto
Condição 3: em até 2x no cartão: preço normal
Condição 4:  3x ou mais no cartão: 20% de juros''')
condição = int(input('\033[32mDigite Aqui a condição de pagamento desejada.\033[m'))
if condição == 1:
    valor = preço - (preço * 10 / 100)
elif condição == 2:
    valor =  preço - (preço * 5 /100)
elif condição == 3:
    valor = preço
    parcela = preço / 2
    print('Parcelado em 2x sem juros com valor da parcela de R$ {:.2f}'.format(parcela))
elif condição == 4:
    valor = preço + (preço * 20 /100)
    numparcelas = int(input('Quantas vezes você quer parcelar'))
    parcela = valor / numparcelas
    print('Compra parcelada em {}x com juros o valor da parcela é de R$ {:.2f}'.format(numparcelas, parcela))
else:
    valor = preço
    print('Opção invalida')
print('O preço da compra é R$ {:.2f} nesta condição de pagamento valor total é R$ {:.2f}'.format(preço, valor))











