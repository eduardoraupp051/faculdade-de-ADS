import random

numero_correto = random.randint(1, 100)
tentativas_restantes = 10

print("tente adivinhar o numero escolhido (entre 1 e 100(): ")

while tentativas_restantes > 0:
    try:
        palpite = int(input("digite seu palpite: "))
    except ValueError:
        print("digite apenas numeros")
        continue

    if palpite == numero_correto
        print("parabens, voce acertou")
        break
    elif palpite < numero_correto
        print("seu palpite é menor do que o correto")
    else:
       print("seu palpite é maior que do que o numero correto")

    tentativas_restantes -= 1

if tentativas_restantes == 0
    print("suas tentaticas acabaram")