#38: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
#O primeiro valor é maior
#O segundo valor é maior
#Não existe valor maior, os dois são iguais
num1 = float(input('Digite o primeiro numero ?'))
num2 = float(input('Digite o segundo numero ?'))
if num1 > num2:
    print(' O primeiro valor {:.1f} é maior que o segundo valor {:.1f}'.format(num1, num2))
elif num2 > num1:
    print('O segundo valor{:.1f} é maior que o primeiro valor {:.1f}'.format(num2, num1))
else:
    print('Os valores são iguais')

