def calcular_media():
    nota = float(input("Informe a sua primeira nota\n(Use . para casas decimais): "))
    nota2 = float(input("Informe a sua segunda nota\n(Use . para casas decimais): "))
    media = (nota + nota2) / 2
    print(f"Sua média aritmética: {round(media, 2)}")
calcular_media()