#46

lista = []
quadrado = []

while True:
    num = int(input("digite um numero para fazer ele ao quadrado ou 0 para finalizar o programa: "))
    if num == 0:
        print("finalizando o programa...")
        break
    else:
        lista.append(num)
for numero in lista:
    quad = numero*numero
    quadrado.append(quad)
print(quadrado)
