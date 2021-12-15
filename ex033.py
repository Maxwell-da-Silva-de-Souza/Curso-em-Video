#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
print('Escreva os numeros para saber qual é maior e o menor.')
a = float(input('Digite um numero...'))
b = float(input('Digite outro...'))
c = float(input('Digite outro ...'))
# verificando o menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# verificando o maior
maior = c
if a > c and a > b:
    maior = a
if b > c and b > a:
    maior = b
print('O menor é {:.2f} e o maior é {:.2f}'.format(menor, maior))




