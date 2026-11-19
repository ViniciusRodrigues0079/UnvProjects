total = 0.0
print("\n Cardápio da lanchonete \n")
print(" Item: Cachorro quente, Código: 100, Preço: R$1,20 ")
print(" Item: Bauru simples, Código: 101, Preço: R$1,30 ")
print(" Item: Bauru com ovo, Código: 102, Preço: R$1,50 ")
print(" Item: Hambúrguer, Código: 103, Preço: R$1,20 ")
print(" Item: Cheeseburguer, Código: 104, Preço: R$1,30 ")
print(" Item: Refrigerante, Código: 105, Preço: R$1,00 \n")
qtd = int(input("Qual a quantidade de produtos que irá pedir? "))
for i in range (0, qtd):
    pedido = int(input("Informe o código do produto a pedir: "))
    if pedido == 100:
        print("+1 Cachorro quente adicionado ao pedido")
        total += 1.2
    elif pedido == 101:
        print("+1 Bauru simples adicionado ao pedido")
        total += 1.3
    elif pedido == 102:
        print("+1 Bauru com ovo adicionado ao pedido")
        total += 1.5
    elif pedido == 103:
        print("+1 Hambúrguer adicionado ao pedido")
        total += 1.2
    elif pedido == 104:
        print("+1 Cheeseburguer adicionado ao pedido")
        total += 1.3
    elif pedido == 105:
        print("+1 Refrigerante adicionado ao pedido")
        total += 1
    else:
        print("Código de produto inválido. Tente novamente.")
    print(f"Total: R${total}0"),
print("Pedido finalizado. Pague no caixa na hora de receber o lanche.")