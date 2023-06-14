nomes = []


#entrada de nomes a lista
while True: 
    nome = input("digite nomes para verificar a quantidade caracteres: ")
    if nome == 'sair': #finaliza a lista
        break
    else:
        nomes.append(nome) #adiciona a lista

#processo para ver se sao todos iguais caralho
primeiro_nome = nomes[0]
igualdade = all(len(nome) == len(primeiro_nome) for nome in nomes)
if igualdade:
    print('certo')
else:
    print('errado')
