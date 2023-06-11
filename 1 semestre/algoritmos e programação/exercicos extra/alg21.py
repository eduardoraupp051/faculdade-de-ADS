num = int(input("digite um numero para calcular a fatorial: "))
fatorial = 1
for i in range (1, num + 1):
    fatorial *= i

print("O fatorial de", num, "é", fatorial)