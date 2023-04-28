while True:

    velocidade_inicial = float(input("digite a velocidade inicial: "))
    acelaracao = float(input("digite o valor da acelaração: "))
    tempo_deslocamento = float(input("digite o tempo de deslocamento: "))
    distancia_percorrida = velocidade_inicial * tempo_deslocamento + 0.5 * acelaracao * (tempo_deslocamento ** 2)

    print("A distância percorrida pelo objeto é: {:.2f} metros".format(distancia_percorrida))