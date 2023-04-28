
valor_inicial = int(input("Digite o valor inicial da aplicação: "))
taxa_juros = int(input("Digite a taxa de juros anual (em porcentagem): "))
tempo_aplicacao = int(input("Digite o tempo de aplicação em anos: "))

taxa_juros_decimal = taxa_juros / 100


valor_final = valor_inicial * (1 + taxa_juros_decimal) ** tempo_aplicacao

print("O valor final da aplicação é: R$", valor_final)
