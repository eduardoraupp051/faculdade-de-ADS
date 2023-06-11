frase = input("Digite uma frase: ")
palavras = frase.split()
frase_invertida = ' '.join(palavras[::-1]) #join serve para uniar letras separadas
print("Frase invertida:", frase_invertida)
