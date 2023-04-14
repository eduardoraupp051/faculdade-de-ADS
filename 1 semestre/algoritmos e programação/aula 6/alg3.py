while True:
    n1 = int(input("digite o numero para verificar se ele é par ou impar: "))
    saber = n1 % 2
    if saber == 0:
        print("o numero é par ")
    else:
        print("o numero é impar")