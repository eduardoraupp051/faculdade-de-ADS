#44
lista = []
while True:
    num = int(input("digite um numero a lista ou digite 0 para finalizar o programa: "))
    if num == 0:
        print("finalizando programa...")
        break
    else:
        lista.append(num)
        lista.sort()
print(f'o segundo numero menor da lista é {lista[1]}')
