lista = []
tamanho = int(input("Digite a quantidade de números que você deseja adicionar à lista: "))

while len(lista) < tamanho:
    num = int(input("Digite um número: "))
    lista.append(num)

pares = [num for num in lista if num % 2 == 0]

print("Os números pares são:", pares)