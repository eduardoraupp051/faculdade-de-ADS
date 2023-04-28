
altura_inicial = float(input("Digite a altura inicial do objeto (em metros): "))


aceleracao_gravidade = 9.81


tempo_queda = (2 * altura_inicial / aceleracao_gravidade) ** 0.5

#
altura_maxima = altura_inicial + ((0 ** 2) / (2 * aceleracao_gravidade))


print(f"A altura máxima alcançada é: {altura_maxima} metros")
print(f"O tempo de queda do objeto é: {tempo_queda}")
