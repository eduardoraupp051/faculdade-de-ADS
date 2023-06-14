lista = []
while True:
    nome = input("digite nome para colocar na lista e ver qual é o mais longo ou sair para finalizar o programa: ")
    lista.append(nome)
    if nome == "sair":
        print("finalizando o programa")
        break
longo = max(lista, key=len)
print("o nome com maiores caractres é", longo)
