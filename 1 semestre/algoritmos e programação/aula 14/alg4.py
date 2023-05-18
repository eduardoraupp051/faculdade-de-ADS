lista = []
tamanho = int(input("digite a quantidade da lista que você quer: "))
while len(lista) < tamanho:

    num = int(input("digite um numero: "))
    
    if num % 2==0:
        lista.append(num)

    elif len(lista) == tamanho:
        break

    print("Os números pares são:", lista)