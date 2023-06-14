lista = []

while True:
    num = int(input('digite numeros para a lista (digite "0" para finalizar): '))
    lista.append(num)
    if num == 0:
        print('finalizando o codigo...')
        break
lista.sort(reverse = True)
print(lista)
