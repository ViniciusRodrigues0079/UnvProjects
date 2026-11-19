def contar_pares():
    total = 0
    qtd = int(input("Informe a quantidade de valores que irá inserir: "))
    for i in range (0, qtd):
        num = int(input("Digite um número inteiro: "))
        if num % 2 == 0:
            total += 1
    print(f"Total de números pares: {total}")
contar_pares()