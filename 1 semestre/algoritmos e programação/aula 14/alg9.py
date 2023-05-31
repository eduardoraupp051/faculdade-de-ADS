num = input("coloque os numeros separados por espaço: ")
lista = [int(lista) for lista in num.split()]

soma = sum(lista)

media = soma / len(lista)

print(f"a media dessa lista é {media}")
-----------------
#Colocando a lista no programa
alunos = []

#Colocando um conjunto (set) no programa. O set serve como uma coleção de itens únicos (distintos), ou seja, torna os IDs dos alunos únicos e exclusivos.
ids_cadastrados = set()

#Loop principal do programa
while True:
    print("Selecione uma opção: ")
    print("1. Criar aluno(a)")
    print("2. Ler alunos")
    print("3. Buscar aluno por ID")
    print("4. Atualizar aluno")
    print("5. Excluir aluno")
    print("0. Sair")
    
    opcao = input("Digite o número da opção desejada: ")
    #Cadastro do aluno
    if opcao == "1": 
        nome = input("Digite o nome do(a) aluno(a): ")
        idade = input(f"Digite a idade do(a) aluno(a) {nome}: ")
        identificador = input(f"Insira o ID desejado para o(a) aluno(a) {nome}: ")
            
        #Caso o ID digitado já pertença a outro discente
        if identificador in ids_cadastrados:
            print ("ID já existente. Digite uma nova ID para o(a) aluno(a).")
            continue
        
        alunos.append((identificador, nome, idade))
        ids_cadastrados.add(identificador)

        continue
    
    #Consultar alunos
    elif opcao == "2":

        if alunos == []:
            print("Nenhum aluno foi cadastrado")

        else:
            for aluno in alunos:
                identificador, nome, idade = aluno
                print(f"ID: {identificador}, Nome: {nome}, Idade: {idade}") 

            continue
    
    #Busca aluno por ID    
    #Busca aluno por ID    
    elif opcao == "3": 
        identificador_desejado = input("Insira o ID do(a) aluno(a) desejado(a): ")

        if alunos == []:
            print("Nenhum aluno foi cadastrado")

        else:
            for aluno in alunos:
                identificador, nome, idade = aluno
                if identificador_desejado == identificador:
                    print(f"ID: {identificador}, Nome: {nome}, Idade: {idade}")


            if identificador_desejado not in ids_cadastrados:
                print(f"Aluno(a) com ID {identificador_desejado} não encontrado(a). Tente novamente!")

    else:
        print("Opção inválida. Por favor, digite novamente.")
        continue