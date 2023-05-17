lista = []
while True:
    nome = input("coloque o nome que voce quer que apareça na lista: ")
    lista.append(nome)
    for nome in lista:
      print(nome)