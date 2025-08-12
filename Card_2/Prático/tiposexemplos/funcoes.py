#Cria o dic
produtos = {}

#Adiciona o produto
def adicionar_produto(nome, preco):
    produtos[nome] = preco
    print("Produto adicionado!")

#Mostra os produtos
def mostrar_produtos():
    print("\nLista de produtos:")
    for nome, preco in produtos.items():
        print(f"{nome} - R${preco:.2f}")

#Consulta os produtos
def consultar_produto(nome):
    if nome in produtos:
        print(f"\nO preço de {nome} é R${produtos[nome]:.2f}")
    else:
        print("\nProduto não encontrado.")

#Programa aplicando função e if/else
if __name__ == "__main__":
    adicionar_produto("Arroz", 5.49)
    adicionar_produto("Maçã", 3.99)

    mostrar_produtos()

    consultar_produto("Arroz")
    consultar_produto("Feijão")
