print("coloque os numeros abaixo para o desconto")
produto = float(input("coloque o valor do produto: "))
desconto = float(input("coloque o valor do desconto: "))
p = produto * (desconto / 100)
valor_final = produto - p
print("o valor do produto é de:", valor_final)