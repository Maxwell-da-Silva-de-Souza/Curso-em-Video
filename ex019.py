#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele,
# lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
from random import choice
n1 = input('Digite o nome do 1º aluno!')
n2 = input('Digite o nome do 2º aluno!')
n3 = input('Digite o nome do 3º aluno!')
n4 = input('Digite o nome do 4º aluno!')
lista = [n1, n2, n3,n4]
print(' O aluno escolhido foi {}'.format(choice(lista)))