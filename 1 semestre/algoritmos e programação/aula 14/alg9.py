num = input("coloque os numeros separados por espaço: ")
lista = [int(lista) for lista in num.split()]

soma = sum(lista)

media = soma / len(lista)

print(f"a media dessa lista é {media}")