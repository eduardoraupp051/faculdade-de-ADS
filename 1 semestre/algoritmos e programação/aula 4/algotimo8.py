import math

lado = int(input("digite o lado do triangulo equilatero: "))
area = (lado ** 2) * math.sqrt(3)/4 #forma de texto importada
area = (lado ** 2) * (3 **0.5)/4 #qualquer numero elevado(potenciação) a ** 0.5 é a raiz
print(area)
