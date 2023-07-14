while True:
    print("Celsius para Fahrenheit [1]")
    print("Celsius para Kelvin [2]")
    print("Fahrenheit para Celsius [3]")
    print("Fahrenheit para Kelvin [4]")
    print("Kelvin para Celsius [5]")
    print("Kelvin para Fahrenheit [6]")
    print("SAIR[7]")
    num = int(input("digite o numero de uma das opções para a conversão: "))

    if num == 0:
        print("você esta saindo do programa: ")

    elif num == 1:
        c = int(input("digite o numero em celcius para a converão em fahrenheit: "))
        fahrenheit = (c * 9/5) + 32
        print("a temperatura de celcius para fahrenheit é", fahrenheit)
    elif num == 2:
        c = int(input("digite o numero em celcius para a converão em KELVIN: "))
        kelvin = c + 273.15
        print("a temperatura de celcius para kelvin é", kelvin)
    elif num == 3:
        f = int(input("digite o numero em fahrenheit para a converão em celcius:"))
        celcius = (f - 32) * 5/9
        print("a temperatura de fahrenheit para celcius é", celcius)

    elif num == 4:
        f = int(input("digite o numero em fahrenheit para a converão em kelvin:"))
        kelvin = (f + 459.67) * 5/9
        print("a temperatura de fahrenheit para kelvin é", kelvin)
    elif num == 5:
        k = int(input("digite o numero em kelvin para a converão em celcius: "))
        celcius =  k - 273.15
        print("a temperatura de kelvin para celcius é", celcius)
    elif num == 6:
        k = int(input("digite o numero em kelvin para a converão em fahrenheit: "))
        fahrenheit =   (k * 9/5) - 459.67
        print("a temperatura de kelvin para fahrenheit é", fahrenheit)




