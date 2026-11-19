def calcular_area():
    largura = float(input("Informe a largura, em metros do terreno da obra\n(utilize . para casas decimais); "))
    comprimento = float(input("Informe o comprimento, em metros do terreno da obra\n(utilize . para casas decimais); "))
    area = largura * comprimento
    print(f"Área do terreno: {round(area, 2)} metros.")
calcular_area()