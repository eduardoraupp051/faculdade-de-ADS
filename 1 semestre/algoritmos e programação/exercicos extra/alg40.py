#40
from time import sleep
lista = []


while True:
    num = int(input("digite um numero para adicionar a lista, e quando finalizar clique 0: "))
    
    
    if num == 0:
        print("finalizando o programa...")
        sleep(1.5)
        break
    if num not in lista:
        lista.append(num)
        
print(lista)
