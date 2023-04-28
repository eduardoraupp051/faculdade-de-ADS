def consultar_aposentadoria():
    mulheres = []
    homens = []
    consulta = 1

    while True:
        print(f"\Consulta número {consulta}")
        nome = input("Digite o nome: ")
        sexo = input("Digite o sexo (M ou F): ").upper()
        idade = int(input("Digite a idade: "))
        tempo_contribuicao = int(input("Digite o tempo de contribuição (em anos): "))

        if sexo == "F":
            if idade >= 55 and tempo_contribuicao >= 30:
                print(f"{nome} pode requerer a aposentadoria!")
                mulheres.append(nome)
            else:
                print(f"{nome} ainda não pode requerer a aposentadoria.")
        elif sexo == "M":
            if idade >= 60 and tempo_contribuicao >= 35:
                print(f"{nome} pode requerer a aposentadoria!")
                homens.append(nome)
            else:
                print(f"{nome} ainda não pode requerer a aposentadoria.")
        else:
            print("Sexo inválido. Por favor, digite M ou F.")
            continue

    
