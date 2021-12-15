#43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa
# calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
#– IMC abaixo de 18,5: Abaixo do Peso
#– Entre 18,5 e 25: Peso Ideal
#– 25 até 30: Sobrepeso
#– 30 até 40: Obesidade
#– Acima de 40: Obesidade Mórbida
print('Bem vindo vamos calcular o seu Indice de massa corporal.')
peso = float(input('Qual é o seu peso em KG ?'))
altura = float(input('Qual é a sua altura em metros ?'))
imc = peso / (altura**2)
print('O seu peso é {} sua altura: {} \033[31mIMC: {:.1f}\033[m '.format(peso, altura, imc))
if imc < 18.5:
    print('Abaixo do Peso.')
elif imc <= 25:
    print('Peso Ideal.')
elif imc <= 30:
    print('Sobrepeso.')
elif imc <= 40:
    print('Obesidade.')
else:
    print('Obesidade Mórbida.')
