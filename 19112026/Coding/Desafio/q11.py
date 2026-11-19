def maior_numero():
    num = int(input("Digite um número inteiro: "))
    num2 = int(input("Digite outro número inteiro: "))
    if num > num2:
        print("O primeiro número é o maior dos dois")
    elif num2 > num:
        print("O segundo número é o maior dos dois")
    else:
        print("Os números são iguais")
maior_numero()