
while True:
    n = input("Digite uma lista de números separados por espaços: ")
    n = n.split()  # Divide a entrada em uma lista de substrings
    n = [int(numero) for numero in n]  

    np = int(input("Digite o número que deseja verificar: "))

    if np in n:
        print("O número", np, "está presente na lista.")
    else:
        print("O número", np, "não está presente na lista.")
