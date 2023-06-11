num = int(input("digite um numero para verificar se ele é primo ou não: "))
if num <= 1:
    print("o numero não é primo")
else:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print("o numero não é primo")
            break
        else: 
            print("o numero é primo")
