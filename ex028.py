# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import choice
from time import sleep
num = int(input('Digite um numero de 0 a 5 para tentar descobrir o numero que eu pensei'))
print('Você degitou o numero {}'.format(num))
lista = [0, 1, 2, 3, 4, 5]
escolhido = choice(lista)
print('=^=' * 25)
print('Processando!!')
sleep(2)
print('=^=' * 25)
print('Parabéns' if num == escolhido else 'tente outra vez !')
print('O numero que pensei foi {}'.format(escolhido))
