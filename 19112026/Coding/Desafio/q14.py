def calcular_compra():
     compra = float(input("Informe o valor total da sua compra\n(use . para casas decimais): "))
     print(f"Valor total da compra após o frete aplicado: ${compra + 15}")
calcular_compra()