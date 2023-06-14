lista = []
while True:
    num = int(input("digite um numero para adicionar na lista ou 0 para sair do programa: "))
    lista.append(num)
    if num == 0:
        print("finalizando...")
        break
crescente = sorted(lista)
print(crescente)
