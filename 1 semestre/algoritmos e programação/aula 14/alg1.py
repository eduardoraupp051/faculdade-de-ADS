lista = []

quantidade = int(input("digite a quantidade de numeros que você quer na lista: "))

for i in range (quantidade):
    num = int(input("digite um numero: "))
    lista.append(num)

maior = max(lista)
print (f"o numero {maior}, é o maior da lista")
