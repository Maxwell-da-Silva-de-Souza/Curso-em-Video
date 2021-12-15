#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
from time import sleep
num = int(input('Digite um valor para saber se ele é par ou ímpar ?'))
print('Processando..')
sleep(1)
valor = num % 2
if valor == 0 :
    print('É um numero par...')
else:
    print('É um numero ímpar ...')

