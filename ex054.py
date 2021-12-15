#54: Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
ano = date.today().year
maior = 0
menor = 0
for pess in range(1, 8):
    nascimento = int(input('Digite ano de nascimento {}º'.format(pess)))
    idade = ano - nascimento
    if idade >= 18:
        maior = maior + 1
    else:
        menor = menor + 1
print('{} pessoas são maiores de idade'.format(maior))
print('{} pessoas são menores de iadade'.format(menor))






