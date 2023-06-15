#47
lista = []

while True:
    num = int(input("digite numeros ou coloque 0 para sair do programa: "))
    
    if num == 0:
        print("finalizando o programa")
        break
    else: 
        lista.append(num)
        
if lista[0] > lista[1]:
    print('esta em ordem descrescente')
else:
    print('esta em ordem crescente')
        
