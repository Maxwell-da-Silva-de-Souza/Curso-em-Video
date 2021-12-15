#Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
largura = float(input(' Digite a largura da parede !!'))
altura = float(input('Digite a altura da parede!!'))
área = largura * altura
tinta = área / 2
print('A área total é {:.3f} metros quadrados  e será necessario {:.3f} litros de tinta '.format(área, tinta))