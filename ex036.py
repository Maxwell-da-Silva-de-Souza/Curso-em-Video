#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
import math

print('Ola seja bem vindo ao simulador para compra da sua nova casa !!')
casa = float(input('Digite o valor da casa desejada ? R$'))
salario = float(input('Digite o valor do seu salario ? R$'))
liquido = salario * 30 / 100
anos = int(input('Em quantos anos você gostaria de pagar?'))
numparcelas = int(anos * 12)
prestação = casa / numparcelas
minparcelas = math.floor(casa / liquido) #contra proposta numero parcelas
#print('min parcelas {}'.format(minparcelas))
if prestação <= liquido:
    print('Parabéns seu financiamento foi aprovado, em \033[31m{}\033[m parcelas '.format(numparcelas),end='')
    print('com valor de R$ \033[31m{:.2f}'.format(prestação))
elif minparcelas * liquido == casa:
    print('Finaciamento negado.')
    print('Para ser aprovado o numero minimo de parcelas \033[31m{}\033[m '.format(minparcelas),end='')
    print('com valor de R$\033[31m {:.2f}'.format(casa / minparcelas))
elif minparcelas * liquido < casa :
    print('\033[34mSeu financiamento foi reprovado.\033[m')
    print('Para ser aprovado. O numero minimo de parcelas é de \033[31m{}\033[m '.format(minparcelas),end='')
    print('Com valor de \033[31m{:.2f}\033[m'.format(((casa - (casa % minparcelas)) / minparcelas)))
    print('sendo acresciddo de mais uma parcela com valor \33[31mR$ {:.2f}\33[m '.format(casa % minparcelas))



