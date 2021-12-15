#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
from math import trunc
num = float(input('Digite um valor !!'))
print('O valor digitado {:.3f} e a parte inteira é {} '.format(num, trunc(num)))

