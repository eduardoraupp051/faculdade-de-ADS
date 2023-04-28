

while True:
    lado1 = float(input("Digite a medida do lado 1 do triângulo: "))
    lado2 = float(input("Digite a medida do lado 2 do triângulo: "))
    lado3 = float(input("Digite a medida do lado 3 do triângulo: "))

    triangulo_valido = False
    
    if lado1 + lado2 > lado3:
        if lado1 + lado3 > lado2:
            if lado2 + lado3 > lado1:
                triangulo_valido = True
    else:
        if triangulo_valido:
            if lado1 == lado2 and lado1 == lado3:
                print("O triângulo é equilátero.")
            elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
                print("O triângulo é isósceles.")
            else:
                print("O triângulo é escaleno.")
        else:
            print("As medidas fornecidas não formam um triângulo válido.")
