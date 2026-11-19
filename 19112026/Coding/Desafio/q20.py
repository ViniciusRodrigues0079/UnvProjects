def calcular_media():
    qtd = int(input("Informe a quntidade de notas para calcular a média: "))
    if qtd > 0:
        notas = []
        tnotas = 0.0
        for i in range (0, qtd):
            notas.append(float(input(f"Informe a {i + 1}ª nota (use . para casas decimais): ")))
        for i in range (0, qtd):
            tnotas += notas[i]
        media = tnotas / len(notas)
        print(f"Notas do aluno: {notas}")
        print(f"Média aritmética do aluno: {round(media, 2)}")
    else:
        print("Valor inválido, o aluno deve ter ao menos uma nota para calcular a média")
calcular_media()