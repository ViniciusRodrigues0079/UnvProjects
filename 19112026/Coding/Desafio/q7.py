def converter_temperatura():
    print("Conversor de Celsius -> Fahrenheit")
    celsius = float(input("Informe a teperatura a ser convertida: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"Temperatura em Fahrenheit: {round(fahrenheit, 2)}")
converter_temperatura()