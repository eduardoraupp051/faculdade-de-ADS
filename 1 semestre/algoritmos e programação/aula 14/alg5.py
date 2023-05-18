lista = []
tamanho = int(input("digite a quantidade da lista que você quer: "))

while len(lista) < tamanho:

    num = int(input("digite um numero: "))
    
    if num % 2==1:
        lista.append(num)
    print("Os números impares são:", lista)