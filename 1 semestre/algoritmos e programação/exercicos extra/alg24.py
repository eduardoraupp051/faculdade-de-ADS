num = input("coloque uma sequencia de numeros para eles erem separados por virgula: ")
nums = num.split(",")
soma_pares = 0

for num in nums:
    if int(num) % 2 == 0:
        soma_pares += int(num)


print("a soma dos numeros pares da sequencia é:", soma_pares)
