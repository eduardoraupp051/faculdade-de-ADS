# Solicita ao usuário uma frase
frase = input("Digite uma frase: ")

# Inicializa a variável contador como 0
contador = 0

# Converte a frase para letras minúsculas para facilitar a contagem
frase = frase.lower()

# Percorre cada caractere da frase
for caractere in frase:
    # Verifica se o caractere é uma vogal
    if caractere in 'aeiou':
        contador += 1

# Exibe a quantidade de vogais encontradas na frase
print("A frase possui", contador, "vogais.")
