#45: Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'tesoura')
computador = randint(0, 2)
print('Vamos jogar Jokenpô')
print(' [0] Pedra\n [1] Papel\n [2] Tesoura')
jogador  = int(input('Digite sua jogada'))
print('Jo')
sleep(0.5)
print('ken')
sleep(0.5)
print('Po')
print('-=' * 15)
print('Computador jogou\033[34m {}\033[m'.format(itens[computador]))
print('Jogador jogou    \033[34m{}\033[m'.format(itens[jogador]))
print('-=' * 15)
if computador == 0:# pedra
    if jogador == 0:# pedra
        print('EMPATE')
    elif jogador == 1:#papel
        print('Você Ganhou')
    elif jogador == 2:# tesoura
        print('Você perdeu')# computador ganhou
    else:
        print('Opção invalida')#usuario digitou numero invalido
elif computador == 1:# papel
    if jogador == 1: #papel
        print('Empate')
    elif jogador == 2: # tesoura
        print('Você ganhou')
    elif jogador == 0: # pedra
        print('Você perdeu')# computador venceu
    else:
        print('Opção invalida')#usuario digitou numero invalido
elif computador == 2: #tessoura
    if jogador == 1: #papel
      print('Você perdeu')# computador venceu
    elif jogador == 0:
        print('Você ganhou')
    elif jogador == 2: # tesoura
        print('Empatou')
    else:
        print('Opçã invalida')


