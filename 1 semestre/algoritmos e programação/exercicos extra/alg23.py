num = input("digite um numero uma sequencia de numeros: ")
nums = num.split()
conv = [int(num) for num in nums]
nums.sort ()
segundo_menor = nums[1]
print(f"o segundo menor numero da lista é {segundo_menor}")