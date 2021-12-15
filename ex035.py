#Desenvolva um programa que leia o comprimento de três retas e
# diga ao usuário se elas podem ou não formar um triângulo
print ('Digite os valores das retas em metros....')
a = float(input('Digite o valor da primeira medida...'))
b = float(input('Digite o valor da segunda medida...'))
c = float(input('Digite o valor da terceira medida...'))
if a < b + c and b < a + c and c < a + b:
    print('As medidas {} metros, {} metros, {} metros pode forma um triangulo.'.format(a, b, c))
else:
    print('As medidas {} metros, {} metros, {} metros não pode formar um triangulo.'.format(a, b, c))

