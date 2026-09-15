"""print ("Algoritmo: Verificando idade")
idade = int(input("Informe a sua idade, em anos: "))
if idade >= 18:
    print ("Você é maior de idade")
else:
    print ("Você é menor de idade")"""

print ("Algoritmo: Conferindo média")
qtdnotas = int(input("Quantas notas você teve ao longo do ano? "))
soma = 0
for i in range (0, qtdnotas):
    nota = float(input(f"Informe a sua {i + 1}ª nota: "))
    soma = soma + nota
media = float(soma / qtdnotas)
print (f"Sua média anual: {round(media, 2)}")