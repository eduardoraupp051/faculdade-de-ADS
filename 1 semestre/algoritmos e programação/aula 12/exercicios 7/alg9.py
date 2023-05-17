while True:
    n = input("coloque os numeros separadamente por espaços para ordernar eles: ")
    n = n.split()
    n = [int(numero) for numero in n]
    n.sort(reverse = True)

    print("A lista em ordem decrescente é:")
    for numero in n:
        print(numero, end=" ")