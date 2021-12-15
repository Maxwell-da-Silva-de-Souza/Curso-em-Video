#51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.
primeiroº = int(input('Digite o primeiro termo da PA.'))
razao = int(input('Digite a razão da PA.'))
décimo = primeiroº + (11 - 1) * razao
for c in range(primeiroº, décimo, razao):
    print('{}'.format(c), end=' ->')
print('Acabou')


