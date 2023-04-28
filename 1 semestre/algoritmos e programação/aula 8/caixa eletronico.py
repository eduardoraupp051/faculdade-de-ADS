
while True:
    valor = int(input("digite o valor de saque: "))

    
    notas_100 = valor // 100
    valor = valor % 100

    notas_50 = valor // 50
    valor = valor % 50

    notas_10 = valor // 10
    valor = valor % 10
   
    notas_5 = valor // 5
    valor = valor % 5

    notas_1 = valor 

    print("valor lido ", valor)

    print("notas 100R$= ", notas_100)

    print("notas 50R$= ", notas_50)

    print("notas 10R$= ", notas_10)

    print("notas 5R$= ", notas_5)
    
    print("notas 1R$= ", notas_1)
