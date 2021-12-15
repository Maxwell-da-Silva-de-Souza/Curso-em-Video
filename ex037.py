#37: Escreva um programa em Python que leia um número inteiro qualquer
# e peça para o usuário escolher qual será a base de conversão:
# 1 para binário, 2 para octal e 3 para hexadecimal.
print('Bem vindo ao conversor de bases numéricas.')
num = int(input('Digite o numero inteiro para fazer a conversão ?'))
print('1 Para binario\n2 Para octal\n3 Para hexadecimal.')
base = int(input('Digite sua opção'))
if base == 1 :
    bin = format(num,'b')
    print(' O numero {} convertido em binario é \033[31m{}'.format(num, bin))
elif base == 2:
    octal = format(num, 'o')
    print(' O numero {} convertido para octal é \033[31m{}'.format(num, octal))
elif base == 3:
    hexadecimal = format(num, "x")
    print(' O numero {} convertido em hexadecimal é \033[31m{}'.format(num, hexadecimal))
else :
    base != 1, 2, 3
    print('\033[31m Codigo de conversão invalido.')





