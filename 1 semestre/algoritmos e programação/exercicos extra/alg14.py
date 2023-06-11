palavra = input("Digite uma palavra: ")
reverso = palavra[::-1]  # Inverte a ordem dos caracteres da palavra

if palavra == reverso:
    print("A palavra é um palíndromo!")
else:
    print("A palavra não é um palíndromo.")
