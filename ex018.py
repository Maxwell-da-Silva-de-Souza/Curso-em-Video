# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math
ângulo = float(input('Digite o valor do ângulo:'))
sen = math.sin(math.radians(ângulo))
print('O ângulo de {:.2f} tem o seno de {:.2f}'.format(ângulo, sen))
cos = math.cos(math.radians(ângulo))
print('O ângulo de {:.2f} tem o cosseno de {:.2f}'.format(ângulo, cos))
tan = math.tan(math.radians(ângulo))
print ('o ângulo de {:.2f} tem a tangente de {:.2f}'.format(ângulo, tan))