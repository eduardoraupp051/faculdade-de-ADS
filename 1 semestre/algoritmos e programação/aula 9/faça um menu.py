while True:
    print("coloque a area de um dos 3 que citarei logo abaixo")
    print("coloque o numero 1 para calcular o circulo")
    print("coloque o numero 2 para calcular o quadrado")
    print("coloque o numero 3 para calcular o retangulo")
    print("coloque o numero 4 para sair")

    opcao = int(input("coloque a opção desejada: "))

    if opcao == 1:
        circulo = int(input("coloque o raio do circulo: "))
        raio = 3.14 * (circulo ** 2)
        print(f"o valor do raio do circulo é {raio}")
        
    elif opcao == 2:
        quadrado = int(input("coloque o raio do quadrado: "))
        area_quadrado = quadrado * quadrado ** 2
        print (f"o valor da area do quadrado é {area_quadrado}")

    elif opcao == 3:
        base = int(input("coloque a area do rentagulo qie deseja calcular: "))
        altura = int(input("coloque a area do rentagulo qie deseja calcular: "))
        area = base * altura
        print (f"a area do retangulo deu {area}")

    elif opcao == 4:
        print("saindo do programa...")
        break

    else:
        print("coloque um numero valido")
        continue
