

contador = 0
while True:
  
    num = int(input("Digite um número entre 1 e 100: "))
    contador = contador + 1
    print("a contagem esta em: ", contador)

    if num % 2 == 0:
     print("O número", num, "é par")
    else:
     print("O número", num, "é ímpar")
 
    if num <= 10:
         print("O número", num, "pertence à primeira dezena")
    elif num <= 20:
        print("O número", num, "pertence à segunda dezena")
    elif num <= 30:
        print("O número", num, "pertence à terceira dezena")
    elif num <= 40:
        print("O número", num, "pertence à quarta dezena")
    elif num <= 50:
        print("O número", num, "pertence à quinta dezena")
    elif num <= 60:
        print("O número", num, "pertence à sexta dezena")
    elif num <= 70:
        print("O número", num, "pertence à sétima dezena")
    elif num <= 80:
        print("O número", num, "pertence à oitava dezena")
    elif num <= 90:
        print("O número", num, "pertence à nona dezena")
    elif num <= 100:
        print("O número", num, "pertence à decima dezena")
    else:
     print("O número", num, "não pertence a nenhuma dezena")
    
