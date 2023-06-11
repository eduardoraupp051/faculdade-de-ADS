num = input("digite a ordem de numeros separada por virgula: ")
nums = num.split(",")
nums_reversos = nums[::-1]

print("Sequência em ordem reversa:", ", ".join(nums_reversos))
