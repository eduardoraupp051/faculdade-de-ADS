lista = []
while True:
    num = int(input(
        "digite um numero para achar o maior em meio a essa lista, quando terminar coloque um 0: "))
    lista.append(num)
    if num == 0:
        print("você saiu do programa")
        break
    
    else:
        maior = max(lista)
        print(lista)

print(maior)