#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta
# e mostre sua categoria, de acordo com a idade:
from datetime import date
atual = date.today().year
nascimento = int(input('Em qual ano você nasceu ?'))
idade = atual - nascimento
print('Você nasceu em {} e tem {} anos em {}'.format(nascimento, idade, atual))
if idade <= 9:
    print(' Você tem {} anos e está na categoria Mirim. '.format(idade))
elif idade > 9 and idade <= 14:
    print('Você tem {} anos e está na categoria Infantil.'.format(idade))
elif idade > 14 and idade <= 19:
    print('Você tem {} anos e está na categoria Júnior.'.format(idade))
elif idade > 19 and idade <= 25:
    print('você tem {} anos e está na categoria Sênior.'.format(idade))
elif idade > 25:
    print('Você tem {} anos e está na categoria Master.'.format(idade))




