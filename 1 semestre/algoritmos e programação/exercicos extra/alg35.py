from time import sleep

lista = []
lista_pares = []

while True:
    num = int(input('digite os numeros da sua lista (digite "0" para finalizar): '))
    lista.append(num)
    if num == 0:
        print('finalizando a lista...')
        sleep(1.5)
        break
for i in lista:
    if i % 2 == 0:
        lista_pares.append(i)
print(f'esse sao os numeros pares de lista {lista_pares}.')
