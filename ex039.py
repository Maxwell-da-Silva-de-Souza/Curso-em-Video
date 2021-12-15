#39: Faça um programa que leia o ano de nascimento de um jovem
# e informe, de acordo com a sua idade,
# se ele ainda vai se alistar ao serviço militar,
# se é a hora exata de se alistar
# ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo
from _datetime import date
ano = date.today().year
print('Bem vindo ao programa de alistamento')
nascido = int(input('Em que ano você nasceu ?'))
idade = ano - nascido
if idade < 18:
    print('Você tem {} anos em {}.'.format(idade, ano))
    print('Terá que se alistar em {} anos'.format(18 - idade))
    print('Deverá se alistar no ano de {}'.format(ano + (18 - idade)))
elif idade == 18:
    print('Você tem {} anos em {} e esta na hora de se alistar, seu ano de alistamento é {}'.format(idade, ano, ano))
elif idade > 18:
    print('Você tem {} anos em {}.'.format(idade, ano))
    print('Deveria ter se alistado em {} anos'.format(idade - 18))
    print('Deveria ter se alistado no ano de {}.'.format(ano - (idade - 18)))

















