consulta = 1
while True:
    print(f"consulta de numero {consulta}")
    print("abaixo digite seu nome, idade, seu sexo, e seu tempo de contribuição")
    nome = (input("digite o seu nome: "))
    sexo = (input("digite o seu sexo: "))
    idade = int(input("digite a sua idade: "))
    tempo_de_trabalho = int(input("digite o seu tempo de trabalho: "))

    if sexo == "masculino":
        if idade >= 60:
            if tempo_de_trabalho >= 35:
                print("voce pode se aposentar")
    elif sexo == "feminino":
        if idade >= 55:
            if tempo_de_trabalho >= 30:
                print("voce pode se aposentar")
    if sexo == "masculino":
        if idade <= 60:
            if tempo_de_trabalho <= 35:
                print("voc0e nao pode se aposentar")
    elif sexo == "feminino":
        if idade <= 55:
            if tempo_de_trabalho <= 30:
                print("voce nao pode se aposentar")    
    
    consulta += 1
    

   