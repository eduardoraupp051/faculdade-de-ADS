#41
lista = []
negativos = []

while True:
    num = int(input('digite os numeros da sua lista (digite 0 para finalizar):'))
    if num == 0:
        lista.append(num)
        print('finalizando')
        break
    elif num < 0:
        negativos.append(num)
print(f'esses sao os numeros negativos {negativos}')
