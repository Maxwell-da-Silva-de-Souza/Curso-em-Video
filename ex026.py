#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”,
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
frase = str(input('Digite a frase !!')).strip()
print('Analizando a frase:')
print('A letra A aparece {} vezes'.format(frase.upper().count('A')))
print('A letra A apareceu primeiro na posição {}'.format(frase.upper().find('A')+1))
print('A ultima vez que a letra A apareceu foi na posição {}'.format(frase.upper().rfind('A')+1))
