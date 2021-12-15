#Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
from time import sleep
from datetime import date
ano = int(input('Digite um ano para saber se ele é bissexto ou não, digite 0 para saber o ano atual ?'))
sleep(0.5)
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é bissexto'.format(ano))
else:
    print('O ano {} não é bissexto'.format(ano))



