#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas e minúsculas.
# Quantas letras ao todo (sem considerar espaços).
# Quantas letras tem o primeiro nome.
#nome = str(input('Digite seu nome:')).strip()
#print('Analisando seu nome')
#print('Seu nome em letras maiusculas é {}'.format(nome.upper()))
#print('Seu nome em letras minusculas é {}'.format(nome.lower()))
#print('Seu nome tem {} letras'.format(len(nome) - nome.count(' ')))
#lista = nome.split()
#print('Seu primeiro nome é {} e tem {}'.format(lista[0], len(lista[0])))
nome = str(input('Digite o deu nome!!')).strip()
print('Analisando seu nome:')
print('Seu nome é {}'.format(nome))
print('seu nome em letras maiusculas {}'.format(nome.upper()))
print('Seu nome em letras minuscula é {}'.format(nome.lower()))
print('Seu nome tem {} letras'.format(len(nome) - nome.count(' ')))
lista = nome.split()
print('Seu primeiro nome é {} tem {} letras.'.format(lista[0], len(lista[0])))
