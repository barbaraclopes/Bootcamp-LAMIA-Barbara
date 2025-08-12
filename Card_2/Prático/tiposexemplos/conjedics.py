# Criando tuplas para representar produtos
produto1 = ("Arroz", "Alimento")
produto2 = ("Detergente", "Limpeza")
produto3 = ("Maçã", "Fruta")

# Dicionário onde a chave é a tupla (nome, categoria) e o valor é o preço
precos = {
    produto1: 5.49,
    produto2: 2.30,
    produto3: 4.99
}

# Mostrando os preços de forma organizada
print("Lista de produtos e preços:")
for produto, preco in precos.items():
    nome, categoria = produto  # Desempacotando a tupla
    print(f"- {nome} ({categoria}): R${preco:.2f}")

# Exemplo de acesso direto
busca = ("Arroz", "Alimento")
if busca in precos:
    print(f"\nPreço do {busca[0]}: R${precos[busca]:.2f}")
else:
    print("\nProduto não encontrado.")
