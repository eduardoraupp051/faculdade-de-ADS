lista = []
quantidade = int(input("coloque a quantidade de palavras que você deseja na lista: "))

for _ in range (quantidade):
    palavra = input("digite uma palavra: ")
    lista.append(palavra)

maior_palavra = max(lista, key=len)

print("A palavra com o maior número de caracteres é:", maior_palavra)