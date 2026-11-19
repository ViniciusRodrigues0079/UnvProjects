produtos = []
def adicionar_produto():
    qtd = int(input("Quantos produtos irá adicionar na lista? "))
    for i in range (0, qtd):
        produtos.append(input("Informe o novo produto: "))
        print (f"Lista atualizada: {produtos}")
adicionar_produto()