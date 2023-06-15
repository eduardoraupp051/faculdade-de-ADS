#43
lista = []
while True:
    num = int(input("digite um numero a lista ou digite 0 para finalizar o programa: "))
    if num == 0:
        print("finalizando programa...")
        break
    else:
        lista.append(num)
        lista.sort(reverse=True)
print(f'o segundo numero maior da lista é {lista[1]}')
