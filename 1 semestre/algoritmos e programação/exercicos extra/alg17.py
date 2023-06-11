# Solicita ao usuário um número para verificar se é perfeito
num = int(input("Digite um número: "))

# Inicializa a variável soma como 0
soma = 0

# Percorre todos os possíveis divisores do número até num // 2
for divisor in range(1, num // 2 + 1):
    if num % divisor == 0:
        soma += divisor

# Verifica se a soma dos divisores é igual ao número
if soma == num:
    print(num, "é um número perfeito.")
else:
    print(num, "não é um número perfeito.")
