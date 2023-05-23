lista = []  # lista vazia para armazenar os números

tamanho = int(input("Digite a quantidade de números que você deseja adicionar à lista: "))

while len(lista) < tamanho:
    numero = int(input("Digite um número: "))
    lista.append(numero)

lista_sem_duplicatas = []  # lista vazia para armazenar os números sem duplicatas

for numero in lista:
    if numero not in lista_sem_duplicatas:  # verifica se o número já está na lista sem duplicatas
        lista_sem_duplicatas.append(numero)

print("A lista sem duplicatas é:", lista_sem_duplicatas)
