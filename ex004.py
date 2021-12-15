# print 'Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo
# e todas as informações possíveis sobre ele.
'''n = input('Digite algo no teclado !  ')
print (' o tipo primitivo desse valor é ' ,type(n))
print (' Alfanumérico ? ' , n.isalnum())
print (' Número ? ', n.isnumeric())
print (' Letra ? ', n.isalpha())
print (' Minuscula ? ', n.islower())
print (' Maiuscula ? ', n.isupper())'''

algo = input('Digite algo no teclado para saber mais sobre ?')
print('o tipo primitivo é ',type(algo))
print('É numero?',algo.isnumeric() )
print('É letra ?',algo.isalpha())
print('É alfanumerico ?',algo.isalnum())
print('É maiuscula ?',algo.isupper())
print('É minuscula ? ',algo.islower())




