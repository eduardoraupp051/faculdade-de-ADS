# Solicita a entrada de nomes ao usuário
entrada = input("Digite uma lista de nomes separados por espaços: ")

# Converte a entrada em uma lista de nomes
nomes = entrada.split()

# Obtém o tamanho do primeiro nome da lista
tamanho = len(nomes[0])

# Utiliza um loop for para verificar se todos os nomes possuem o mesmo tamanho
todos_mesmo_tamanho = True
for nome in nomes:
    if len(nome) != tamanho:
        todos_mesmo_tamanho = False
        break

# Imprime o resultado
if todos_mesmo_tamanho:
    print("Todos os nomes possuem a mesma quantidade de caracteres.")
else:
    print("Os nomes possuem tamanhos diferentes.")

#codigo não feito por mim