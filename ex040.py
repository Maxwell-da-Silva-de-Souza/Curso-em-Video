#040: Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média atingida:
nota1 = float(input('Digite a primeira nota.'))
nota2 = float(input('Digite a segunda nota.'))
média  = (nota1 + nota2)/2
print('primeria nota {} Segunda nota {} Média {}.'.format(nota1, nota2, média))
if média < 5:
    print('Reprovado média abaixo de 5.00 sua média foi de \033[31m{:.2f}'.format(média))
elif média >= 7:
    print('Aprovado média  maior ou igual a 7 sua média foi de \033[31m{:.2f}'.format(média))
else:
    print('Recuperação média entre 5 e 7 sua média foi de \033[31m{:.2f}'.format(média))