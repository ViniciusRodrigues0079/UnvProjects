"""z = []
z.append(15)
z.append(8)
z.append(9)
print(z)
z[0] = 7
print(z)
print(z[0])"""

"""notas = [6, 7, 5, 8, 9]
soma = 0
for i in range (0, 5):
    soma += notas[i]
print (f"Média: {round(soma/5, 2)}")"""

"""vetor = []
for i in range (0, 5):
    vetor.append(int(input("Digite um número inteiro: ")))
print (f"Vetor lido: {vetor}")"""

"""z = [15, 8, 9, 5, 3]
a = z.pop(3)
print (a)
print(z)
b = z.pop()
print(b)
print(z)"""

"""z = [15, 8, 9, 5, 3]
print(z.index(8))
z = [15, 8, 9, 5, 8]
print (z.count(8))
z = [15, 8, 9, 5, 3]
z.sort ()
print(z)
z.sort (reverse=True)
print(z)
z = [15, 8, 9, 5, 3]
z.reverse()
print(z)"""


#Desafio 1

"""z = []
for i in range(0, 10): #1
    z.append(i+1)
print (z)

del(z[2]) #2
print(z)

del(z[z.index(5)]) #3
print (z)

z.append(11) #4
z.append(12)
print (z)

z.insert(0, 0) #5
print (z)

print (f"Tamanho da lista Z: {len(z)}") #6

z = []
for i in range(0, 10): #1
    z.append(i+1)
print (z)"""


#Desafio 2

"""z = []
soma = 0

for i in range(0, 8):
    z.append(int(input("Digite um número inteiro: ")))
for i in range(0, 8):
    soma += z[i]

print (f"Média dos valores digitados: {round(soma/len(z), 2)}")
print (f"Soma dos valores digitados: {soma}")

z.sort()
print (f"Menor valor: {z[0]}")
z.sort(reverse=True)
print (f"Maior valor: {z[0]}")"""


#Desafio 2.Menu

"""z = []
r = 0
while r != 6:
    r = int(input((f"\nMenu de funções: \n\n Digite 1 para inserir um novo valor \n Digite 2 para recalcular a média \n Digite 3 para recalcular a soma \n Digite 4 para recalcular o maior valor \n Digite 5 para recalcular o menor valor \n Digite 6 para fechar o menu \n\n Seus números na lista: {z} \n\n Qual função irá executar? ")))
    if r == 1:
        z.append(int(input("\nDigite um número inteiro: ")))
    elif r == 2:
        soma = 0
        for i in range(0, len(z)):
            soma += z[i]
        media = soma / len(z)
        print(f"\nMédia: {media}")
    elif r == 3:
        soma = 0
        for i in range(0, len(z)):
            soma += z[i]
        print(f"\nSoma: {soma}")
    elif r == 4:
        z.sort(reverse=True)
        print (f"\nMaior valor: {z[0]}")
    elif r == 5:
        z.sort()
        print (f"\nMenor valor: {z[0]}")
    elif r== 6:
        print ("\nMenu fechado.\n")
    else:
        print("\nFunção inválida. Tente novamente.")"""

z = ["João", 8, 5, [1, 2, 3, 4]] # Lista dentro de lista
print (z[3])
print (len(z))
print (len(z[3]))
print (z [3] [1]) # Imprimir um item de uma lista que está dentro de outra