num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

temp = num1  # Armazena o valor de num1 temporariamente

num1 = num2  # Atribui o valor de num2 a num1
num2 = temp  # Atribui o valor temporário a num2

print("O valor do primeiro número digitado é", num1)
print("O valor do segundo número digitado é", num2)
