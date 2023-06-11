sequencia = input("Digite uma sequência de números separados por vírgula: ")
numbers = sequencia.split(",")
numbers = [int(num) for num in numbers]  # Convertendo os números de string para inteiros

max_number = max(numbers)
print("O maior número da sequência é:", max_number)
