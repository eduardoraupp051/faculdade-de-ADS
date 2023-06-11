lista = []
while True:
    num = int(input(
        "digite um numero para achar o menor em meio a essa lista, quando terminar coloque um 0: "))
    lista.append(num)
    if num == 0:
        print("você saiu do programa")
        break
    
    else:
        menor = min(lista)
        print(lista)

print(menor)