lista = []

while True:

    num = input("coloque os numeros que voce quer que apareçam separados por espaço: ")
    num = num.split()

    for num in num:
        n = int(num)
        if n % 3 == 0 and n % 5 == 0:
            lista.append(n)
            print(n)


    print("Os números múltiplos de 3 e 5 são:", lista)