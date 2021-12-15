#'Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.'
n = float (input('Digite um numero!'))
print('''Analizando o numero {:.2f}
 o dobro é           {:.2f}
 o triplo é          {:.2f}
 e a raiz quadrada é {:.2f}'''.format(n, (n*2), (n*3), (n**0.5)))