"""frutas = []
mult = 1
for i in range (0, 4):
    frutas.append(int(input("Informe um número inteiro: ")))
for i in range (0,4):
    mult = mult * frutas[i]
media = (mult ** (1/4))
print (f"sua média é: {media}")"""


"""frutas = []
invfrutas = []
soma = 0
for i in range (0,3):
    frutas.append(int(input("Informe um número inteiro: ")))
for i in range (0,3):
    invfrutas.append(1 / frutas[i])
for i in range (0,3):
    soma += invfrutas[i]
media = 3 / soma
print (f"sua média é: {media}")"""


"""frutas = []
for i in range (0,3):
    frutas.append(int(input("Informe um número inteiro: ")))
for i in range (0,3):
    if frutas[i] % 2 == 0:
        print ("True")
    else:
        print ("False")"""


"""nota1 = nota2 = 0
nota1 += float(input("Informe a sua primeira nota: "))
nota2 += float(input("Informe a sua Segunda nota: "))
media = (nota1 + nota2) / 2
if media >= 7:
    print("Äprovado")
else:
    print("Reprovado")"""


#Escreva 4 números, imprima True se o primeiro + o terceiro = segundo - quarto, false caso contrário


#


"""num1 = int(input("Informe um número inteiro: "))
num2 = int(input("Informe outro número inteiro: "))
if num1 > num2:
    print ("O primeiro  número digitado é o maior")
elif num2 > num1:
    print ("O segundo número digitado é o maior")"""


"""cidade = str(input("Qual a cidade em que você nasceu? "))
if cidade == "Recife":
    print("Recifense?")
elif cidade == "Olinda":
    print("Olindense?")
else:
    print("Legal!")"""


import random
jogada1 = random.randint(0, 10)
jogada2 = random.randint(0, 10)
print (f"\n \n \nPrimeira jogada: {jogada1}")
print (f"Segunda jogada: {jogada2}")
soma = jogada2 + jogada1
if soma % 2 == 0:
    print("O jogador de pares vence!\n \n \n")
else:
    print("O jogador de ímpares vence!\n \n \n")

# Em uma brincadeira de par ou ímpar virtual, dois jogadores devem informar os valores (entre 0 e 10) de sua "jogada".
# Estes números devem ser gerados de forma aleatória (não devem ser gerados previamente ou recebidos pelo teclado), 
# e ao final, deve imprimir o valor da jogada de cada um e se o número é par ou ímpar