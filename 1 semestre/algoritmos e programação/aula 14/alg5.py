num1 = input("Digite uma lista de números separados por espaços: ")
numeros = [int(numero) for numero in num1.split()]
quantidade_impares = 0

for numero in numeros:
    if numero % 2 == 1:
        quantidade_impares += 1

print("A quantidade de números pares na lista é:", quantidade_impares)