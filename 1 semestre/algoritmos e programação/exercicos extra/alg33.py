lista = []

while True:
    num = int(input("Digite números para adicionar à lista (ou 0 para encerrar): "))
    if num == 0:
        break
    lista.append(num)

numero_verificar = int(input("Digite o número que deseja verificar na lista: "))

if numero_verificar in lista:
    print("O número", numero_verificar, "está presente na lista.")
else:
    print("O número", numero_verificar, "não está presente na lista.")
