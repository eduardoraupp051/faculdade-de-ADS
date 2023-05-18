lista = []
quantidade = int(input("digite quantos numeros a lista vai somar: "))

for i in range (quantidade):
    num = int(input("digite um numero: "))
    lista.append(num)

soma = sum(lista)
print("a soma dos numeros da lista é", soma)
      

