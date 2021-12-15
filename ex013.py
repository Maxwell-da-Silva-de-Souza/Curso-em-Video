#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario = float(input(' Digite o salario atual !! R$'))
novo = salario + (salario * 15 / 100)
print (' O salario atual é R$ {:.2f} com aumento de 15% R$ {:.2f}'.format(salario, novo))