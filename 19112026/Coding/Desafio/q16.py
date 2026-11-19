def calcular_imc():
    peso = float(input("Informe o seu peso, em quilogramas\n(utilize . para casas decimais): "))
    altura = float(input("Informa a sua altura, em metros\n(utilize . para casas decimais): "))
    imc = peso / (altura ** 2)
    print(f"Seu IMC: {round(imc, 1)}")
calcular_imc()