lista = []

while True:
    num = input("coloque os numeros separados por espaço: ")
    num = num.split()

    for num in num:
        n = int(num)
        if n % 3 == 0 and n % 5 == 0:
            lista.append(n)
            print(n)

    print("os numeros multiplos de 3 e 5 são:", lista)

