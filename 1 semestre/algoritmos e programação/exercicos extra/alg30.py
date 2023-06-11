lista = []
while True:
    num = int(input("digite numeros para calcular na lista: "))
    lista.append(num)
    if num == 0:
        print("você saiu do programa")
        break
    else:
        soma = sum(lista)
        print(lista)
    
print((f"o numero total das listas é {soma}"))