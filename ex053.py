# 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
# desconsiderando os espaços. Exemplos de palíndromos:
# APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA
frase = str(input('Digite a frase para saber se ela é um palíndromo.')).strip().upper()
lista = frase.split()
juntar =''.join(lista)
inverso = ''
for letra in range(len(juntar)-1, -1, -1):
    inverso = inverso + juntar[letra]
print('Você digitou {} e escrito ao contrario é {} '.format(juntar, inverso))
if inverso == juntar:
    print('Temos um palíndromo')
else:
    print('Não é um palíndromo')




