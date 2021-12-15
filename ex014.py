#Escreva um programa que converta uma temperatura digitando em graus Celsius
# e converta para graus Fahrenheit.
Celsius = float(input('Didite a temperatura em C° !!'))
Fahrenheit = (Celsius * (9 / 5 )) + 32
print (' A temperatura em  {:.2f} C° e equivale em  {:.2f} F°'.format(Celsius, Fahrenheit))
