#Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o último nome separadamente.
nome = str(input('Escreva seu nome!!')).strip()
lista = nome.split()
print(' O seu primeiro nome é {}\n O seu ultimo nome é {}'.format(lista[0], lista.pop()))
