def somar_vendas():
    soma = 0.0
    qtd = int(input("Qual a quantidade de vendas realizadas durante a semana? "))
    for i in range (0, qtd):
        soma += (float(input(f"Informe o preço da {i + 1}ª venda\n(utilize . para casas decimais): ")))
    print(f"Valor total arrecadado em vendas: ${round(soma, 2)}")
somar_vendas()