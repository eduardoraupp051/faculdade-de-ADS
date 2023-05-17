lista = []

while len(lista) < 10:

    num = int(input("digite um numero: "))
    if num % 2==1:
        lista.append(num)

    print("Os números impares são:", lista)