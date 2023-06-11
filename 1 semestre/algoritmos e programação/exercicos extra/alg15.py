num = int(input("Digite um número: "))

# Verifica se o número é menor ou igual a 1
if num <= 1:
    print("O número não é primo.")
else:
    # Percorre os números de 2 até a raiz quadrada do número
    for i in range(2, int(num**0.5) + 1):
        # Verifica se o número é divisível por algum número dentro desse intervalo
        if num % i == 0:
            print("O número não é primo.")
            break
    else:
        print("O número é primo.")
