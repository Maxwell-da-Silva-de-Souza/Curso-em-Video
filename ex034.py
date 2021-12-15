# Escreva um programa que pergunte o salário de um funcionário
# e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.
salario = float(input('Digite o seu salario para saber quanto aumentará...'))
if salario > 1250.00:
   salario =  salario + (salario * 10 / 100)
else:
    salario = salario + (salario * 15 / 100)
print('O seu novo salario será de R$ \033[1;30;47m {:.2f}\033[m'.format(salario))


