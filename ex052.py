#52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
num = int(input('Digite um numero'))
total = 0
for c in range(1, num + 1):
        if num % c == 0 :
            print('\033[31m{}\033[m'.format(c), end=' -')
            total = total + 1
        else:
            print('\033[35m{}\033[m'.format(c),end=' -')
if total > 2:
    print('\nO numero {} foi divisivel por {} numeros'.format(num, total))
    print('Por este motivo \033[31mNÃO É PRIMO\033[m')
else:
    print('\nO numero {} foi divisivel somente por {} numeros'.format(num, total))
    print('Por este motivo \033[31mÉ UM NUMERO PRIMO\033[m')

