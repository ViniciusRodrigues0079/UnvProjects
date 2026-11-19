def somar():
    num = float(input("Digite o primeiro número a ser somado\n(use . para casas decimais): "))
    num2 = float(input("Digite o segundo número a ser somado\n(use . para casas decimais): "))
    soma = num + num2
    print(f"Resultado da soma (arredondado): {round(soma, 2)}")
somar()