#42: Refaça o DESAFIO 35 dos triângulos,
# acrescentando o recurso de mostrar que tipo de triângulo será formado:
from time import sleep
a = float(input('Digite a primeira medida.'))
b = float(input('Digite a segunda medida.'))
c = float(input('Digite a terceira medida.'))
print('Analizando')
sleep(0.5)
if a < b + c and b < c + a and c < a + b:
    print('As medidas forma um triangulo')
    if a == b == c:
        print('Triangolo do tipo Equilatero')
    elif a != b and a != c or b != c and b != a or c != a and c != b: # a != b != c != a
        print('Triangulo do tipo Escaleno')
    #elif a == b and a != c or b == c and b != a or c == a and c != b:# criei o cod porêm foi necessario .
    else:
        print('Triangulo do tipo Isóceles')
else:
    print('As medidas não podem formar um triangulo.')





