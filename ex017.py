#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
# Calcule e mostre o comprimento da hipotenusa.
from math import hypot
co = float(input('Digite o valor do cateto oposto:'))
ca = float(input( 'Digite o valor do cateto adjacente:'))
'''hi = ((co**2 + ca**2)**0.5)
print('O valor da hipotenusa {:.2f} '.format(hi))'''
hi = hypot(co, ca)
print(' Ovalor da hipotenusa {:.2f} '.format(hi))