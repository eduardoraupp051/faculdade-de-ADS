lista = []
quantidade = int(input("coloque a quantidade de numeros pra lista: "))


for i in range (quantidade):
    num = int(input("digite um numero: "))
    lista.append(num)

menor = min(lista)
print("o menor numero da lista é", menor)