lista = []

while len(lista) < 10:

    num = int(input("digite um numero: "))
    if num % 2==0:
        lista.append(num)

    print("Os números pares são:", lista)