
while True:
    n = input("coloque os numeros separadamente por espaços para ordernar eles: ")
    n = n.split()
    n = [int(numero) for numero in n]
    n.sort()

    print("A lista em ordem crescente é:")
    for numero in n:
        print(numero, end=" ")