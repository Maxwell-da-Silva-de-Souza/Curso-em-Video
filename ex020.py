#O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random
n1 = str(input('Digite o nome do aluno:'))
n2 = str(input('Digite o nome do aluno:'))
n3 = str(input('Digite o nome do aluno:'))
n4 = str(input('Digite o nome do aluno:'))
list = [n1, n2, n3, n4]
random.shuffle(list)
print ('A ordem de apresentação escolhida é {}'.format(list))