lista = []  # lista vazia para armazenar os números
tamanho = int(input("Digite a quantidade de números que você deseja adicionar à lista: "))

while len(lista) < tamanho:
    numero = int(input("Digite um número: "))
    lista.append(numero)

impares = []  # lista vazia para armazenar os números ímpares

i = 0  # contador para iterar sobre os elementos da lista

while i < len(lista):
    if lista[i] % 2 != 0:  # verifica se o número é ímpar
        impares.append(lista[i])
    i += 1

print("Os números ímpares são:", impares)
