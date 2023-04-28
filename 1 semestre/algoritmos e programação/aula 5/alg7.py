
while True:

    peso = float(input("coloque seu peso: "))
    altura = float(input("coloque sua altura: "))
    IMC = peso // altura**2

    if IMC <= 18.4:
        print("voce esta abaixo do peso")
    elif IMC >= 18.5 and IMC <= 24.9:
        print("Voce esta com o peso adequado")
    elif IMC >= 25.0 and IMC <= 29.9:
        print("Voce esta sobrepeso")
    elif IMC >= 30.0 and IMC <= 34.9:
        print("Voce esta com o peso gordox")
    elif IMC >= 35.0 and IMC <= 39.9:
        print("voce esta em nivel critico")
    else:
        print("voce esta muito gordo")

    print(f"seu IMC {IMC}")