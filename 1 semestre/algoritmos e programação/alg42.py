#42
lista = []
while True:
    num = int(input("digite um numero para somar os impares ou digite 0 para finalizar o programa: "))
    if num == 0:
        print("finalizando programa...")
        break
    elif num % 2 == 1:
        lista.append(num)
impares = sum(lista)
        
print("a soma dos numeros impares dessa lista é", impares)
