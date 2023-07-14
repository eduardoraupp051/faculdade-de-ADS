while True:
    print("para verificar a aprovação, digite [1]")
    print("para sair do programa digite [0]")
    num = int(input("escolha uma das opções: "))
    if num == 0:
        print("Você esta saindo do programa...")
    elif num == 1:
        nome = input("digite seu nome: ")
        ap1 = int(input("digite o valor da sua AP1(ate 1,5 ): "))
        ap2 = int(input("digite o valor da sua AP2(ate 2,5): "))
        ass = int(input("digite o valor da sua AS(ate 6): "))
        faltas = int(input("digite o seu numero de faltas de 1 a 24: "))
        ps = ap1 + ap2 + ass

        if faltas > 5:
            print(f"Infelizmente {nome}, você foi reprovado por faltas..")
        elif ps >= 6 and faltas <= 5:
            print(f"Parabéns, {nome}, você foi aprovado!")
        elif ps < 6 and faltas <=5:
            print(f"{nome}, você deverá fazer a Avaliação Final (AF)")
    
