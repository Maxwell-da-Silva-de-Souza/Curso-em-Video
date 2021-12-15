#' Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.'
n = float(input('Digite um valor em metros!'))
print(' O valor em metros {:.2f} em centimetros {:.2f} em milimetros {:.2f}'.format(n, (n*10), (n*1000)))