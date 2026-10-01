print("Calculadora\n")
op = str(input("Escolha a operação desejada:\n(S = soma, M= subtração, X = multiplicação, D = divisão)\n"))
num1 = float(input("Diga um número: "))
num2 = float(input("Diga um número para somar, subtrair, multiplicar ou dividir: "))
if op in "SsMmXxDd":
    if op in "Ss":
        resultado = num1 + num2
    elif op in "Mm":
        resultado = num1 - num2
    elif op in "Xx":
        resultado = num1 * num2
    else:
        resultado = num1 / num2
    print(f"Resultado da sua operação: {round(resultado, 2)}")
else:
    print("Operação inválida. Tente novamente.")