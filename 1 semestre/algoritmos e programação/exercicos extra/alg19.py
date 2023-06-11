num = input("Digite um número: ")
num_digits = len(num)
armstrong_sum = sum(int(digit)**num_digits for digit in num)

if armstrong_sum == int(num):
    print(num, "é um número de Armstrong.")
else:
    print(num, "não é um número de Armstrong.")
