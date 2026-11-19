def calcular_desconto():
    preço = float(input("Informe o preço do produto a se aplicar o desconto\n(utilize . para casas decimais): "))
    percentual = int(input("Informe o percentual de desconto do produto: "))
    valor = preço *  percentual / 100
    valor = preço - valor
    print(f"Valor do produto após o desconto: ${round(valor, 2)}")
calcular_desconto()